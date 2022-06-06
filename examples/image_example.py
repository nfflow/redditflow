from redditflow import ImageApi


config = {
        "sort_by": "best",
        "subreddit_image_limit": 3,
        "total_limit": 10,
        "start_time": "13.11.2021 09:38:42",
        "end_time": "15.11.2021 11:38:42",
        "subreddit_search_term": "cats",
        "subreddit_object_type": "comment",
        "client_id": "$CLIENT_ID",  # get client id for praw
        "client_secret": '$CLIENT_SECRET',  # get client secret for praw
         }

ImageApi(config)
