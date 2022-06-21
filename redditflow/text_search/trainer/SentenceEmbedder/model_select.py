class ModelSelect:

    def __init__(self, model_name, model_output_path,
                 model_architecture='CT'):
        self.model_architecture = model_architecture
        self.model_name = model_name
        self.model_output_path = model_output_path

    def return_trainer(self):
        model_architecture = self.model_architecture.lower()
        model_name = self.model_name
        model_output_path = self.model_output_path
        if model_architecture == 'ct':
            from .contrastive_tension import ContrastiveTensionTrainer
            trainer = ContrastiveTensionTrainer(model_name,
                                                model_output_path)
            return trainer
        elif model_architecture == 'simcse':
            from .simcse import SimCSETrainer
            trainer = SimCSETrainer(model_name,
                                    model_output_path)
            return trainer
        elif model_architecture == 'tsdae':
            from .tsdae import TsdaeTrainer
            trainer = TsdaeTrainer(model_name,
                                   model_output_path)
            return trainer
        else:
            print('model architecture not found in available architectures')
