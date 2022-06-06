from .txt_utils import scrape_data, sort_scraped
from ...text_search import Classify
from ...text_search.trainer import ModelSelect
import os
from datetime import datetime
import time


class TextApi:
    def __init__(self, config):
        if "end_time" in config.keys():
            end_time = config['end_time']
            time1 = datetime.strptime(end_time,
                                      "%d.%m.%Y %H:%M:%S").timestamp()
            time2 = datetime.now().timestamp()
            # if end time is atleast 10 mins from now
            if time1-time2 > 600:
                newtime = datetime.now().timestamp()
                while time1 - newtime > 300:
                    time.sleep(300)
                    new_endtime = newtime + 300
                    config['end_time'] = new_endtime
                    print('''starting Cron Job
                          for scraping data from your future......''')
                    data, save_timestamp = scrape_data(config)
                    classifier = Classify()
                    sort_scraped(config, classifier, data, save_timestamp)

        data, save_timestamp = scrape_data(config)
        classifier = Classify()
        sort_scraped(config, classifier, data, save_timestamp)

        if "ml_pipeline" in config.keys():
            ml_config = config['ml_pipeline']
            model_name = ml_config['model_name']
            model_output_path = ml_config['model_output_path']

            if 'model_architecture' in ml_config.keys():
                model_architecture = ml_config['model_architecture']
                if 'CT' in model_architecture:
                    trainer = ModelSelect(model_name,
                                          model_output_path).return_trainer()
            else:
                trainer = ModelSelect(model_name,
                                      model_output_path).return_trainer()

            trainer.train(data_path=os.path.join(
                save_timestamp, 'scraped_classified.json'))
