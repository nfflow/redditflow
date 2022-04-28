from datetime import datetime
import requests
import time
import json


class RedditScraper:
    def __init__(self, config):
        if "author" not in config and "subreddit" not in config:
            raise ValueError("Fill in either username or subreddit")
        self.filter_string = "&"
        for k, v in config.items():
            if v:
                self.filter_string += str(k) + "=" + str(v) + "&"

    def scrape(self, object_type, start_time=None, end_time=None, limit=1000):
        data = []
        count = 0
        previous_epoch = int(datetime.utcnow().timestamp())

        limit_flag = False

        url = "https://api.pushshift.io/reddit/{}/search?limit={}&sort=desc{}before={}"
        if start_time:
            url = "https://api.pushshift.io/reddit/{}/search?limit={}&sort=desc{}before={}&after={}"
        while True:
            if start_time:
                if end_time:
                    new_url = url.format(
                        object_type, limit, self.filter_string, end_time, start_time
                    )
                else:
                    new_url = url.format(
                        object_type,
                        limit,
                        self.filter_string,
                        str(previous_epoch),
                        start_time,
                    )
            else:
                new_url = url.format(
                    object_type, limit, self.filter_string, str(previous_epoch)
                )
            json_text = requests.get(
                new_url, headers={
                    "User-Agent": "Post downloader by /u/Watchful1"}
            )
            time.sleep(
                1
            )  # pushshift has a rate limit, if we send requests too fast it will start returning error messages
            try:
                json_data = json_text.json()
            except json.decoder.JSONDecodeError:
                time.sleep(1)
                print("JSONDecodeError")
                continue
            if "data" not in json_data:
                break
            objects = json_data["data"]
            if len(objects) == 0:
                break
            for object in objects:
                previous_epoch = object["created_utc"] - 1
                if end_time:
                    end_time = previous_epoch
                count += 1
                if object_type == "comment":
                    try:
                        data.append(
                            object["body"]
                            .encode(encoding="ascii", errors="ignore")
                            .decode()
                        )
                        if len(data) >= limit:
                            print(
                                "Subreddit limit reached, stopped collecting comments..."
                            )
                            limit_flag = True
                    except Exception as err:

                        print("Couldn't get comment")
                        print(err)
                elif object_type == "submission":
                    if object["is_self"]:
                        if "selftext" not in object:
                            continue
                        try:
                            data.append(
                                object["selftext"]
                                .encode(encoding="ascii", errors="ignore")
                                .decode()
                            )
                            if len(data) >= limit:
                                print(
                                    "Subreddit limit reached, stopped collecting submissions..."
                                )
                                limit_flag = True
                        except Exception as err:
                            print("Couldn't get post")
                            print(err)

            print(
                "Saved {} {}s through {}".format(
                    len(data),
                    object_type,
                    datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d"),
                )
            )

            if limit_flag:
                break
        return data
