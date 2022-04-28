from reflow.image_search import redditImageScraper, ImageSearch
import shutil
from datetime import datetime, timedelta
import os
from reflow import SubredditSearch

config = {"subreddit_image_limit": 20, "total_limit": 100, "sort_by": "top",
          "start_time": "13.11.2021 09:38:42", "end_time": "15.11.2021 11:38:42", "subreddit_search_term": "cats", "subreddit_object_type": "submission", "client_id": "R_7GuGx7LpvXDYqTaOc7cA",
          "client_secret": "Vcb2V1TDjs1QH6nPQD3u3Klni0GKmQ",
          "user_agent": 'Multithreaded Reddit Image Downloader v2.0 (by u/impshum)'}


def scrape_images(config, image_datastore_dir="image_datastore"):
    if "subreddit_search_term" in config.keys() and "subreddits" in config.keys():
        raise AttributeError(
            "Add one of 'subreddit_search_term' or 'subreddits' to config")
    if "subreddit_search_term" not in config.keys() and "subreddits" not in config.keys():
        raise AttributeError(
            "Add either 'subreddit_search_term' or 'subreddits' to config")

    object_type = config["subreddit_object_type"]
    if config["start_time"]:
        start_time = datetime.strptime(config["start_time"],
                                       '%d.%m.%Y %H:%M:%S')
    else:
        start_time = None
    if config["end_time"]:
        end_time = datetime.strptime(config["end_time"],
                                     '%d.%m.%Y %H:%M:%S')
    else:
        end_time = None

    if "subreddits" in config.keys():
        subreddits = config["subreddits"]
    elif "subreddit_search_term" in config.keys():
        sub_search = SubredditSearch()
        subreddit_search_term = config["subreddit_search_term"]
        subreddits = sub_search.search(
            subreddit_search_term, object_type, start_time=start_time, end_time=end_time)

    total_images = 0  # count total images which got scraped
    for subreddit in subreddits:
        img_scraper = redditImageScraper(subreddit, config["subreddit_image_limit"], config["sort_by"], client_id=config["client_id"],
                                         client_secret=config["client_secret"], user_agent=config["user_agent"], img_datastore=image_datastore_dir)
        if end_time:
            pass  # write code to stop cron job when date is end time
        img_scraper.start(start_time=start_time)
        total_images += config["subreddit_image_limit"]
        if total_images >= config["total_limit"]:
            subreddits = [i for i in os.listdir(
                image_datastore_dir) if i in subreddits]
            break
    return subreddits, image_datastore_dir


def image_classify(config):
    subreddits, img_datastore = scrape_images(config)
    print(subreddits)
    output_paths = []
    for subreddit in subreddits:
        search = ImageSearch(img_dir=os.path.join(
            os.getcwd(), img_datastore+"/"+subreddit))
        output_paths.append(search.search(
            config["subreddit_search_term"], k=config["subreddit_image_limit"], threshold_score=0.5))
    return output_paths


output_paths = image_classify(config)
out = []
for path in output_paths:
    out += path
if not os.path.exists('filtered_images'):
    os.mkdir('filtered_images')
for path in out:
    shutil.copy(path, 'filtered_images/')
