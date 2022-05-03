# Reflow. 

## Mission.
Scrape data from reddit over a period of time of your choice, filter with AI assistants, and connect it to your ML pipelines!

## Installation.  
`pip install reflow`

## Docs.  
### Text API.  
Argument | Input | Description
--------- | ------- | -----------  
sort_by | str | Sort the results by available options like 'best', 'new' ,'top', 'controversial' , etc as available from Reddit.
subreddit_text_limit | int | Number of rows to be scraped per subreddit
total_limit | int | Total number of rows to be scraped
start_time | DateTime | Start date and time in dd.mm.yy hh.mm.ss format
stop_time | DateTime | Stop date and time in dd.mm.yy hh.mm.ss format
subreddit_search_term | str | Input search term to create filtered outputs
subreddit_object_type | str | Available options for scraping are `submission` and `comment`

## Example

### Text Scraping and filtering
```
config = {
        "sort_by": "best",
         "subreddit_text_limit": 50,
        "total_limit": 200,
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




