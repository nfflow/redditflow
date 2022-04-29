class Classify:

    def __init__(self, classifier_algorithm="zero_shot", model=None):
        self.classifier_algorithm = classifier_algorithm

        if classifier_algorithm == "cosine_similarity":
            if not model:
                model = "paraphrase-multilingual-MiniLM-L12-v2"
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model)
        else:
            from transformers import pipeline
            if not model:
                model = "cross-encoder/nli-deberta-v3-small"
            self.model = pipeline(task="zero-shot-classification", model=model)

    def return_tag(self, textlist, labels, threshold_score=0.5):

        if self.classifier_algorithm == "cosine_similarity":
            from sentence_transformers import util
            text_embeds = self.model.encode(textlist, convert_to_tensor=True)
            label_embeds = self.model.encode(labels, convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(text_embeds, label_embeds)
            text = []
            classes = []

            for index in range(len(cosine_scores)):
                for i in range(len(cosine_scores[index])):

                    if cosine_scores[index][i] > threshold_score:
                        text.append(textlist[index])
                        classes.append(labels[i])

            return {"text": text, "label": classes}

        else:

            pipe = self.model
            labels += ["other"]
            res = pipe(textlist, labels)
            text = []
            classes = []

            for i in range(len(res)):

                if max(res[i]["scores"]) > threshold_score:
                    label = res[i]["labels"]
                    [res[i]["scores"].index(max(res[i]["scores"]))]

                    if label != "other":
                        text.append(res[i]["sequence"])
                        classes.append(label)

            return {"text": text, "label": classes}
