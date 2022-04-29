from .txt_utils import scrape_data, sort_scraped
from ...text_search import Classify


class TextApi:
    def __init__(self, config):
        data, save_timestamp = scrape_data(config)
        classifier = Classify()
        sort_scraped(config, classifier, data, save_timestamp)
