import pandas as pd
from datetime import datetime
from ...text_search import RedditScraper, SubredditSearch
import os


def scrape_data(config, write_to_file="json"):

    save_timestamp = str(int(datetime.now().timestamp()))
    if "subreddit_search_term" not in config.keys():
        if "subreddits" not in config.keys():
            raise AttributeError(
                "Add either 'subreddit_search_term' or 'subreddits' to config"
            )

    object_type = config["subreddit_object_type"]

    if config["start_time"]:
        start_time = datetime.strptime(config["start_time"],
                                       "%d.%m.%Y %H:%M:%S")
    else:
        start_time = None
    if config["end_time"]:
        end_time = datetime.strptime(config["end_time"], "%d.%m.%Y %H:%M:%S")
    else:
        end_time = None

    if "subreddits" in config.keys():
        subreddits = config["subreddits"]

    elif "subreddit_search_term" in config.keys():
        sub_search = SubredditSearch()
        subreddit_search_term = config["subreddit_search_term"]
        print("searching for subreddits......")
        subreddits = sub_search.search(
            subreddit_search_term, object_type,
            start_time=start_time, end_time=end_time
        )

    data = []
    subreddit_names = []
    finished_rows = 0

    resume_task_timestamp = None
    if "resume_task_timestamp" in config.keys():
        resume_task_timestamp = config["resume_task_timestamp"]
    # check for finished subreddit files

    if resume_task_timestamp:

        resume_task_timestamp = str(resume_task_timestamp)
        files = os.listdir(resume_task_timestamp)
        finished_subreddits = [i.replace(".json", "")
                               for i in files if i.endswith(".json")]
        finished_rows = sum([len(pd.read_json(
            os.path.join(resume_task_timestamp, i)
        )) for i in files if i.endswith(".json")]
        )
        config["total_limit"] = config["total_limit"] - finished_rows

        subreddits = [i for i in subreddits if i not in finished_subreddits]
        save_timestamp = resume_task_timestamp

        print("resuming from checkpoint "
              + resume_task_timestamp +
              "..... " + str(finished_rows) + "data points processed already")

    for subreddit in subreddits:
        print(subreddit)
        config["subreddit"] = subreddit
        r = RedditScraper(config)
        try:
            subreddit_data = r.scrape(
                object_type,
                start_time=start_time,
                end_time=end_time,
                limit=config["subreddit_text_limit"],
            )

            subreddit_names += [subreddit for i in range(len(subreddit_data))]
            data += subreddit_data

            if write_to_file:

                if not os.path.exists(save_timestamp):
                    os.mkdir(save_timestamp)

                pd.DataFrame({"text": data,
                              "subreddit": subreddit_names}).to_json(
                    os.path.join(save_timestamp, subreddit + ".json")
                )

            print(str(len(data)+finished_rows)+" data points collected")
            if len(data) >= config["total_limit"]:
                break
        except Exception as e:
            print(e)
            continue

    scraped_outputs = pd.DataFrame({"text": data, "subreddit": subreddit_names})

    if write_to_file:
        scraped_outputs.to_json(os.path.join(save_timestamp,
                                             "scraped_full.json"),
                                orient="records",
                                lines=True)

    return scraped_outputs, save_timestamp


def sort_scraped(config, classifier, data, save_timestamp):

    def _clean_data(data):

        remove_terms = ["", "[removed]"]
        out = data[~data['text'].isin(remove_terms)]

        return out

    if "subreddit_search_term" in config.keys():
        data = _clean_data(data)
        print(data, len(data))
        subreddit_search_term = [config["subreddit_search_term"]]
        out = classifier.return_tag(
            list(data["text"]), subreddit_search_term,
        )
        pd.DataFrame(out).to_json(os.path.join(save_timestamp,
                                               "scraped_classified.json"),
                                  orient="records",
                                  lines=True)
