# Image API

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