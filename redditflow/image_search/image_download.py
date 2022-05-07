import os
import re
import requests
import praw
import configparser
import concurrent.futures
import argparse
from datetime import datetime, timedelta


class redditImageScraper:
    def __init__(self, sub, limit, order, client_id, client_secret, user_agent, nsfw=False, img_datastore="images"):
        config = configparser.ConfigParser()
        config.read('conf.ini')
        self.sub = sub
        self.limit = limit
        self.order = order
        self.nsfw = nsfw
        self.path = f'{img_datastore}/{self.sub}/'
        self.reddit = praw.Reddit(
            client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    def download(self, image):
        r = requests.get(image['url'])
        with open(image['fname'], 'wb') as f:
            f.write(r.content)

    def start(self, start_time=None, remove_existing=True):
        images = []
        start_time = datetime.timestamp(start_time)
        go = 0
        if self.order == 'hot':
            submissions = self.reddit.subreddit(self.sub).hot(limit=None)
        elif self.order == 'top':
            submissions = self.reddit.subreddit(self.sub).top(limit=None)
        elif self.order == 'new':
            submissions = self.reddit.subreddit(self.sub).new(limit=None)
        elif self.order == 'best':
            submissions = self.reddit.subreddit(self.sub).best(limit=None)

        for submission in submissions:
            if not submission.stickied and submission.over_18 == self.nsfw \
                    and submission.url.endswith(('jpg', 'jpeg', 'png')):
                if start_time:
                    created_time = datetime.utcfromtimestamp(
                        submission.created_utc)
                    created_time = datetime.timestamp(created_time)

                    if created_time >= start_time:
                        fname = self.path + \
                            re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                        if not os.path.isfile(fname):
                            images.append(
                                {'url': submission.url, 'fname': fname})
                            go += 1
                            if go >= self.limit:
                                break
                else:
                    fname = self.path + \
                        re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                    if not os.path.isfile(fname):
                        images.append({'url': submission.url, 'fname': fname})
                        go += 1
                        if go >= self.limit:
                            break
        if len(images):
            if remove_existing:
                if os.path.exists(self.path):
                    for file in os.listdir(self.path):
                        os.remove(os.path.join(self.path, file))
                    os.rmdir(self.path)
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            with concurrent.futures.ThreadPoolExecutor() as ptolemy:
                ptolemy.map(self.download, images)
