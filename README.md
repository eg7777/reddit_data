
# Reddit Scraper: Quick Start Guide


This script scrapes Reddit posts and their comments using the Reddit API. Follow these steps to configure and run the script.


1\. Set Up Reddit API Credentials

Create a new application if you don't already have one:

Client ID
Client Secret
Username
Password
User Agent (e.g., python\:my\_reddit\_scraper\:v1.0 (by /u/your\_username)).


2\. Configure config.json


Update the config.json file with your credentials and desired settings. Below is an example configuration file:

{

&#x20;   "client\_id": "your\_client\_id",

&#x20;   "client\_secret": "your\_client\_secret",

&#x20;   "user\_agent": "python\:my\_reddit\_scraper\:v1.0 (by /u/your\_username)",

&#x20;   "username": "your\_username",

&#x20;   "password": "your\_password",

&#x20;   "reddit\_thread": "funny",

&#x20;   "max\_post": 1000,

&#x20;   "start\_post": 5,

&#x20;   "end\_post": 15,

&#x20;   "filename": "funny.json"

}


Configuration Fields:

client\_id: Your Reddit API client ID.
client\_secret: Your Reddit API client secret.
user\_agent: A unique identifier for your application.
username: Your Reddit username.
password: Your Reddit password.
reddit\_thread: The subreddit you want to scrape (e.g., worldnews).
max\_post: Maximum number of posts to scrape (limit to <=1000).
filename: The name of the output file (e.g., worldnews.json).



3\. Install Dependencies


Ensure Python is installed, then install the required library:



pip install praw



4\. Run the Script



Save the script and config.json in the same directory.



Execute the script:



python your\_script\_name.py



5\. Output



The scraped data will be saved in the file specified by the filename field in config.json (e.g., tesla.json).Notes

- Modify `reddit_thread` to scrape a different subreddit.
- Adjust `max_post` to control the number of posts to scrape (limit to <=1000) 

---


