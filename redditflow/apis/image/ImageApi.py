from .img_utils import scrape_images, image_classify
import os
import shutil


class ImageApi:
    def __init__(self, config, image_datastore_dir='image_datastore',
                 dest_dir='filtered_images'):
        subreddits, img_datastore = scrape_images(config, image_datastore_dir)
        output_paths = image_classify(config, subreddits, img_datastore)

        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)

        os.mkdir(dest_dir)

        for path in output_paths:
            shutil.copy(path, dest_dir)
