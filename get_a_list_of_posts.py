# simple script to get a list of posts from a user
# this is a test script to get the hang of the atproto library

from atproto import Client, client_utils
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')


client = Client()
client.login(username, password)


# Get the timeline
timeline = client.get_timeline()

# Iterate through the posts in the timeline
for post in timeline.feed:
    print(f"Author: {post.post.author.handle}")
    print(f"Text: {post.post.record.text}")
    print("---")