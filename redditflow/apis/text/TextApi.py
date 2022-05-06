from .txt_utils import scrape_data, sort_scraped
from ...text_search import Classify
from ...text_search.trainer import ContrastiveTensionTrainer
import os


class TextApi:
    def __init__(self, config):
        data, save_timestamp = scrape_data(config)
        classifier = Classify()
        sort_scraped(config, classifier, data, save_timestamp)

        if "ml_pipeline" in config.keys():
            ml_config = config['ml_pipeline']
            model_name = ml_config['model_name']
            model_output_path = ml_config['model_output_path']

            trainer = ContrastiveTensionTrainer(model_name,
                                                model_output_path)

            trainer.train(data_path=os.path.join(
                save_timestamp, 'scraped_classified.json'))
