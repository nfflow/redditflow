import os
import json
from redditflow import TextApi, ImageApi


output_dir = "/app/output"

def load_config(api_type):
    if api_type == "text":
        config_file_path = os.environ.get("config")
        if config_file_path and os.path.exists(config_file_path):
            with open(config_file_path,"r") as config_file:
                config=json.load(config_file)
        else:
            config= {

                "sort_by":os.environ.get("sort_by", "top"),
                "subreddit_image_limit":os.environ.get("subreddit_text_limit", "50"),
                "total_limit": os.environ.get("total_limit", "200"),
                "start_time": os.environ.get("start_time", "13.11.2021 09:38:42"),
                "end_time": os.environ.get("end_time", "15.11.2021 11:38:42"),
                "subreddit_search_term":os.environ.get("subreddit_search_term", "cats"),
                "subreddit_object_type": os.environ.get("subreddit_object_type", "comment"),
                "model_name":os.environ.get("model_name", "distilbert-base-uncased"),
            "model_output_path":os.environ.get("model_output_path", "healthcare_27.03.2021-27.03.2022_redditflow"),
            'model_architecture':os.environ.get("model_architecture", "CT"),
                }
    elif api_type == "image":
        config_file_path = os.environ.get("config")
        if config_file_path and os.path.exists(config_file_path):
            with open(config_file_path,"r") as config_file:
                config=json.load(config_file)
        else:
            config= {

                "sort_by":os.environ.get("sort_by", "top"),
                "subreddit_image_limit":os.environ.get("subreddit_image_limit", "3"),
                "total_limit": os.environ.get("stotal_limit", "10"),
                "start_time": os.environ.get("start_time", "13.11.2021 09:38:42"),
                "end_time": os.environ.get("end_time", "15.11.2021 11:38:42"),
                "subreddit_search_term":os.environ.get("subreddit_search_term", "cats"),
                "subreddit_object_type": os.environ.get("subreddit_object_type", "comment"),
                "user_agent": os.environ.get("user_agent","dummy"),
                "client_id":os.environ.get("client_id",  "$CLIENT_ID"),  
                "client_secret":os.environ.get("client_secret", '$CLIENT_SECRET'), 
                }
            
    else:
        raise ValueError("Invalid API type selected.")
    return config

def main():
    api_type = os.environ.get("API_TYPE", "text")
    config = load_config(api_type)

    # Use the selected API type and its configuration
    if api_type == "text":
        text=TextApi(config)
    elif api_type == "image":
        image=ImageApi(config)
    else:
        raise ValueError("Invalid API type selected.")


if __name__ == "__main__":
    main()