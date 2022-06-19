import math
from sentence_transformers import models, losses
from sentence_transformers import SentenceTransformer
import pandas as pd


class ContrastiveTensionTrainer:
    def __init__(self,
                 model_name,
                 model_output_path,
                 batch_size=16,
                 pos_neg_ratio=8,
                 num_epochs=1,
                 max_seq_length=75,
                 device=None):

        self.model_name = model_name
        self.batch_size = batch_size
        self.pos_neg_ratio = pos_neg_ratio
        self.num_epochs = num_epochs
        self.max_seq_length = max_seq_length
        self. model_output_path = model_output_path

        word_embedding_model = models.Transformer(
            self.model_name, max_seq_length=self.max_seq_length
            )
        pooling_model = models.Pooling(
            word_embedding_model.get_word_embedding_dimension())

        self.model = SentenceTransformer(modules=[word_embedding_model,
                                                  pooling_model],
                                         device=device)

    def train(self, data_path,
              steps_per_epoch=100000,
              warmup_steps=0.1,
              optimizer_params={'lr': 2e-5},
              weight_decay=0,
              scheduler='WarmupLinear',
              show_progress_bar=True,
              use_amp=False):

        num_epochs = self.num_epochs
        model = self.model
        model_output_path = self.model_output_path

        data = pd.read_json(data_path, lines=True)
        train_sentences = data["text"]
        train_dataloader = losses.ContrastiveTensionDataLoader(
            train_sentences, batch_size=self.batch_size,
            pos_neg_ratio=self.pos_neg_ratio)

        train_loss = losses.ContrastiveTensionLoss(model)
        warmup_steps = math.ceil(
            len(train_dataloader) * num_epochs * warmup_steps)

        # Train the model
        model.fit(train_objectives=[(train_dataloader, train_loss)],
                  steps_per_epoch=steps_per_epoch,
                  warmup_steps=warmup_steps,
                  optimizer_params=optimizer_params,
                  weight_decay=weight_decay,
                  scheduler=scheduler,
                  checkpoint_path=model_output_path,
                  show_progress_bar=show_progress_bar,
                  use_amp=use_amp
                  )
