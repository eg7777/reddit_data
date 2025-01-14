
# Reddit Scraper: Quick Start Guide


This script scrapes Reddit posts and their comments using the Reddit API. Follow these steps to configure and run the script.


1. Set Up Reddit API Credentials

To get started, create a Reddit application if you don't already have one. Visit Reddit App Preferences to create the app and take note of your credentials.


2.  Configure config.json


Update the config.json file with your credentials and desired settings. Below is an example configuration file:

```
{
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "user_agent": "python:my_reddit_scraper:v1.0 (by /u/your_username)",
    "username": "your_username",
    "password": "your_password",
    "reddit_thread": "funny",
    "max_post": 1000,
    "start_post": 1,
    "end_post": 1000,
    "filename": "funny.json"
}

```

Configuration Fields:

- client\_id: Your Reddit API client ID.
- client\_secret: Your Reddit API client secret.
- user\_agent: A unique identifier for your application.
- username: Your Reddit username.
- password: Your Reddit password.
- reddit\_thread: The subreddit you want to scrape (e.g., worldnews).
- max\_post: Maximum number of posts to scrape (limit to <=1000).
- filename: The name of the output file (e.g., worldnews.json).
- start_post or end_post: Ignore for now



3.   Install Dependencies


Ensure Python is installed, then install the required library:


```
pip install praw
```


4.   Run the Script



Save the script and config.json in the same directory.



Execute the script:


```
python your\_script\_name.py
```


5.  Output



The scraped data will be saved in the file specified by the filename field in config.json (e.g., tesla.json).Notes

- Modify `reddit_thread` to scrape a different subreddit.
- Adjust `max_post` to control the number of posts to scrape (limit to <=1000) 

---


