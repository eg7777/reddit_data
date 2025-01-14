import praw
import json
import time


# Load credentials from the config file
with open("config.json") as config_file:
    config = json.load(config_file)

# Initialize Reddit instance using the credentials from the config file
reddit = praw.Reddit(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    user_agent=config["user_agent"],
    username=config["username"],
    password=config["password"],
)

# Access a subreddit
subreddit = reddit.subreddit(config["reddit_thread"])

# Initialize a list to store all posts and their comments
posts_data = []
max_posts = config["max_post"]  # Set an upper limit to control the total number of posts (adjust as needed)
posts_retrieved = 0  # Counter to keep track of posts retrieved

# Start pagination with the 'new' sorting method
for post in subreddit.new(limit=None):  
    # Stop if we've reached the desired number of posts
    if posts_retrieved >= max_posts:
        break
    
    # Dictionary to hold the post data
    post_data = {
        "title": post.title,
        "score": post.score,
        "url": post.url,
        "description": post.selftext,
        "created": post.created_utc,
        "category": post.link_flair_text,
        "comments_count": post.num_comments,
        "comments": []
    }
    
    # Load all comments, including replies
    post.comments.replace_more(limit=0)  # Removes "MoreComments" placeholders
    
    # Process each top-level comment
    for comment in post.comments:
        comment_data = {
            "comment_body": comment.body,
            "replies": []
        }
        
        # Process each reply to the comment
        if comment.replies:
            for reply in comment.replies:
                reply_data = {
                    "reply_body": reply.body
                }
                comment_data["replies"].append(reply_data)
        
        # Append the comment data to the post's comments list
        post_data["comments"].append(comment_data)
    
    # Append the post data to the main list
    posts_data.append(post_data)
    posts_retrieved += 1  # Increment the post counter

    # Print progress every 100 posts
    if posts_retrieved % 100 == 0:
        print(f"{posts_retrieved} posts scraped so far...")

    # Sleep to handle rate limits
    time.sleep(3)

# Save the data to a JSON file
with open(config["filename"], "w") as json_file:
    json.dump(posts_data, json_file, indent=4)

print(f'Data saved to {config["filename"]}')
