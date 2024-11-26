from atproto import Client, client_utils
from dotenv import load_dotenv
import sqlite3
import time 
import os

# load environment variables
load_dotenv()

# get blue sky credentials
username = os.getenv('username')
password = os.getenv('password')

# connect to blue sky
client = Client()
client.login(username, password)

# Set up SQLite database
conn = sqlite3.connect('bsky_posts.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT,
        text TEXT
    )
''')
conn.commit()

print("Database setup complete. Starting feed...")
# Keep track of the most recent post we've seen
last_seen_post = None

while True:
    try:
        # Get the timeline
        timeline = client.get_timeline(limit=50)  # Adjust limit as needed

        # Iterate through posts, newest first
        for post in reversed(timeline.feed):
            # If we've seen this post before, skip to the next one
            if last_seen_post and post.post.cid == last_seen_post:
                break
            
            # Insert post into database
            cursor.execute('''
                INSERT INTO posts (author, text) VALUES (?, ?)
            ''', (post.post.author.handle, post.post.record.text))
            
            # Print post details
            print(f"Author: {post.post.author.handle}")
            print(f"Text: {post.post.record.text}")
            print("---")

        # Commit the changes to the database
        conn.commit()

        # Update the last seen post
        if timeline.feed:
            last_seen_post = timeline.feed[0].post.cid

        # Wait for a bit before checking again
        time.sleep(60)  # Wait for 60 seconds
        
    except KeyboardInterrupt:
        print("\nExiting the feed loop...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Waiting before trying again...")
        time.sleep(300)  # Wait for 5 minutes before trying again

# Close the database connection
conn.close()
print("Database connection closed. Exiting program.")