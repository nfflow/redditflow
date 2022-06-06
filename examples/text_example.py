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
