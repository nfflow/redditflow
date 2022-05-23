from .img_utils import scrape_images, image_classify
import os
import shutil
from datetime import datetime
import time


class ImageApi:
    def __init__(self, config, image_datastore_dir='image_datastore',
                 dest_dir='filtered_images'):
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
                    print('starting Cron Job for scraping data from your future......')
                    subreddits, img_datastore = scrape_images(config,
                                                              image_datastore_dir)
                    output_paths = image_classify(config,
                                                  subreddits, img_datastore)
                exit()
        subreddits, img_datastore = scrape_images(config, image_datastore_dir)
        output_paths = image_classify(config, subreddits, img_datastore)

        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)

        os.mkdir(dest_dir)

        for path in output_paths:
            shutil.copy(path, dest_dir)
