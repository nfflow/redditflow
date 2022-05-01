# Reflow. 

## Mission.
Scrape data from reddit over a period of time of your choice, filter with AI assistants, and connect it to your ML pipelines!

## Installation.  
`pip install reflow`

## Docs
  
  
## Example

### Text Scraping and filtering
```
config = {
        "sort_by": "best",
        "total_limit": 200,
        "subreddit_text_limit": 50,
        "start_time": "27.03.2021 11:38:42",
        "end_time": "27.03.2022 11:38:42",
        "subreddit_search_term": "healthcare",
        "subreddit_object_type": "comment",
        # "resume_task_timestamp":1648613439
    }
from reflow import TextApi
TextApi(config)
```
### Image Scraping and filtering

```
config = {"subreddit_image_limit": 3, "total_limit": 10, "sort_by": "top",
          "start_time": "13.11.2021 09:38:42", "end_time": "15.11.2021 11:38:42", "subreddit_search_term": "cats", "subreddit_object_type": "comment", "client_id": "$CLIENT_ID", # get client id for praw
          "client_secret": $CLIENT_SECRET, #get client secret for praw
         }

from reflow import ImageApi
ImageApi(config)

```




