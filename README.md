# Redditflow. 

## Mission.
Scrape data from reddit over a period of time of your choice, filter with AI assistants, and connect it to your ML pipelines!

Execution is as simple as this: 

* Make a config file with your required details of input.
* Run the API in a single line with the config passed as input.

## Installation.  
`pip install redditflow`

## Docs.  
### 1) Text API.  

Argument | Input | Description
--------- | ------- | -----------  
sort_by | str | Sort the results by available options like 'best', 'new' ,'top', 'controversial' , etc as available from Reddit.
subreddit_text_limit | int | Number of rows to be scraped per subreddit
total_limit | int | Total number of rows to be scraped
start_time | DateTime | Start date and time in dd.mm.yy hh.mm.ss format
stop_time | DateTime | Stop date and time in dd.mm.yy hh.mm.ss format
subreddit_search_term | str | Input search term to create filtered outputs
subreddit_object_type | str | Available options for scraping are `submission` and `comment`. 
resume_task_timestamp | str, Optional | If task gets interrupted, the timestamp information available from the created folder names can be used to resume.
ml_pipeline | Dict, Optional | If an ML pipeline needs to be connected at the end, to have a trained model, specify this parameter

### 2) Image API

Argument | Input | Description
--------- | ------- | -----------  
sort_by | str | Sort the results by available options like 'best', 'new' ,'top', 'controversial' , etc as available from Reddit.
subreddit_image_limit | int | Number of images to be scraped per subreddit
total_limit | int | Total number of images to be scraped
start_time | DateTime | Start date and time in dd.mm.yy hh.mm.ss format
stop_time | DateTime | Stop date and time in dd.mm.yy hh.mm.ss format
subreddit_search_term | str | Input search term to create filtered outputs
subreddit_object_type | str | Available options for scraping are `submission` and `comment`
client_id | str | Since Image API requires praw, the config requires a praw client ID.
client_secret | str | Praw client secret. 

## Examples

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
         "resume_task_timestamp":1648613439
    }
from redditflow import TextApi
TextApi(config)
```
### Image Scraping and filtering

```
config = {
        "sort_by": "best",
        "subreddit_image_limit": 3,
        "total_limit": 10,
         "start_time": "13.11.2021 09:38:42",
         "end_time": "15.11.2021 11:38:42",
         "subreddit_search_term": "cats",
         "subreddit_object_type": "comment",
         "client_id": "$CLIENT_ID", # get client id for praw
         "client_secret": $CLIENT_SECRET, #get client secret for praw
         }

from redditflow import ImageApi
ImageApi(config)

```




