# Redditflow. 

<div align="center">

<img src="./misc/redditflow.jpeg" width="25%" height="25%" width="400px">

**Do everything from data collection from reddit to training a machine learning model in just two lines of python code!  **

______________________________________________________________________

<p align="center">
  <a href="https://www.nfflow.com/">Website</a> •
  <a href="#installation">Installation</a> •
  <a href="https://github.com/nfflow/redditflow/tree/main/docs">Docs</a> •
  <a href="https://huggingface.co/NFflow">Huggingface Hub</a> •
  <a href="https://huggingface.co/NFflow](https://dev.to/abhijithneilabraham/redditflow-find-data-from-any-timeline-from-past-to-future-and-feed-your-ml-pipelines-jnh)">Blog</a> •
     
</p>


[![PyPI Status](https://badge.fury.io/py/redditflow.svg)](https://badge.fury.io/py/redditflow)
[![Downloads](https://pepy.tech/badge/redditflow)](https://pepy.tech/project/redditflow)
![Build Status](https://github.com/nfflow/redditflow/actions/workflows/build.yml/badge.svg)
[![Discord](https://img.shields.io/discord/982008844261658726)](https://discord.gg/8JSx2THB45)
[![license](https://img.shields.io/pypi/l/redditflow)](https://github.com/nfflow/redditflow/blob/master/LICENSE)

</div>
   
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
        "user_agent": "dummy",
        "client_id": "$CLIENT_ID",  # get client id for praw
        "client_secret": '$CLIENT_SECRET',  # get client secret for praw
         }

ImageApi(config)


```

Since the image api requires praw api from python, a praw `client_id` and `client_secret` are required. [Read here](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/) about how to get client id and client secret for praw.
   
# Citation. 

If you use our work, please cite the software in the url: https://github.com/nfflow/redditflow
