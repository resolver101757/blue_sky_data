from atproto import Client, client_utils
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')



def main():
    client = Client()
    profile = client.login(username, '48ckQo9h0p!e2MgE')
    print('Welcome,', profile.display_name)
    
    text = client_utils.TextBuilder().text('Hello World from ').link('Python SDK', 'https://atproto.blue')
    post = client.send_post(text)
    client.like(post.uri, post.cid)


if __name__ == '__main__':
    main()