# Redditflow. 

Huggingface-hub - [View our example models on huggingface hub!](https://huggingface.co/NFflow)   
Blog - [Read a short blog about our mission and how redditflow works!](https://dev.to/abhijithneilabraham/redditflow-find-data-from-any-timeline-from-past-to-future-and-feed-your-ml-pipelines-jnh).  

Join our discussions in Discord! [Join by clicking here](https://discord.gg/8u362Yc3)



## Mission.
Do everything from data collection from reddit to training a machine learning model in just two lines of python code!   

Supports:

- Text Data
- Image Data

Execution is as simple as this: 

* Make a config file with your required details of input.
* Run the API in a single line with the config passed as input.

## Installation.  
`pip install redditflow`
### Latest installation from source.  
`pip install git+https://github.com/nfflow/redditflow`

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
ml_pipeline | Dict, Optional | If an ML pipeline needs to be connected at the end, to have a trained model, specify this parameter. [How to specify ML pipeline arguments](#ML-Pipeline-Arguments)




#### ML pipeline arguments
The ML pipeline dict can have the following arguments.

Argument | Input | Description
--------- | ------- | -----------  
model_name | str | path to pre-trained model name(Currently from Sentence Transformers (https://www.sbert.net/) hub.   
model_output_path | str | path to the model_output

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

### Text data collection and training a model in the end.
```
from redditflow import TextApi


config = {
        "sort_by": "best",
        "subreddit_text_limit": 50,
        "total_limit": 200,
        "start_time": "27.03.2021 11:38:42",
        "end_time": "27.03.2022 11:38:42",
        "subreddit_search_term": "healthcare",
        "subreddit_object_type": "comment",
        "ml_pipeline": {
            'model_name': 'distilbert-base-uncased',
            'model_output_path': 'healthcare_27.03.2021-27.03.2022_redditflow',
            'model_architecture': 'CT'
            }
    }


TextApi(config)


```
### Image data collection

```
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


```

Since the image api requires praw api from python, a praw `client_id` and `client_secret` are required. [Read here](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/) about how to get client id and client secret for praw.



