# Text API.  

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
