import requests


class SubredditSearch:
    def search(self, query, object_type, start_time=None, end_time=None):
        if start_time:
            if end_time:
                url = "https://api.pushshift.io/reddit/search/{}/?q={}&before={}&after={}"
                url = url.format(object_type, query, end_time, start_time)
            else:
                url = "https://api.pushshift.io/reddit/search/{}/?q={}&after={}"
                url = url.format(object_type, query, start_time)
        else:
            url = "https://api.pushshift.io/reddit/search/{}/?q={}"
            url = url.format(object_type, query)
        json_text = requests.get(
            url, headers={'User-Agent': "Abhijith"}, verify=False).json()
        subreddits = [data["subreddit"] for data in json_text["data"]]
        return subreddits
