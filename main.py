import google.generativeai as genai
from fasthtml.common import *
from dotenv import load_dotenv
import sqlite3
import os

app, rt = fast_app()

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
google_api_key = os.getenv('google_api_key')
genai.configure(api_key=google_api_key)

# query the llm
def analyze_feed_topics(posts):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b",
        generation_config=generation_config,
        )

    chat_session = model.start_chat(
        history=[]
    )

    my_bsky_posts = ""
    # remove this later 
    for post in posts[:5]:
        my_bsky_posts += f"Author: {post[0]}\nText: {post[1]}\n"

    llm_text = "this is a list of posts from blue sky, please analyze the data and return a list of topics that are being discussed/n" + my_bsky_posts
    response = chat_session.send_message(llm_text)

    print(response.text)
    return response.text


def read_sky_data():
    """Read data from bsky_posts.db SQLite database"""
    conn = sqlite3.connect('bsky_posts.db')
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT author, text FROM posts')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()
        
        
@rt("/")
def get():
    return (
        Title("Blue Sky Reports"),
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
        Style("""
            .loader {
                border: 4px solid #f3f3f3;
                border-radius: 50%;
                border-top: 4px solid #3498db;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        """),
        Body(
            Div(
                Header(
                    H1("Blue Sky Feed Analysis", cls="text-3xl font-bold text-center"),
                    P("Analyzing your Blue Sky social feed using AI", cls="text-center mt-2 text-blue-100"),
                    cls="bg-gradient-to-r from-blue-500 to-blue-700 text-white p-6 mb-6 rounded-lg shadow-lg"
                ),
                Div(
                    Button(
                        "Analyze My Feed",
                        id="generate-query-btn",
                        cls="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition duration-300 shadow-md",
                        hx_post="/generate-query",
                        hx_target="#query-result",
                        hx_indicator="#loading-indicator"
                    ),
                    cls="mb-8 text-center"
                ),
                Div(
                    Div(cls="loader mr-2"),
                    Span("Analyzing your feed...", cls="text-gray-600"),
                    id="loading-indicator",
                    cls="hidden flex justify-center items-center my-4"
                ),
                Div(
                    H2("Analysis Results", cls="text-xl font-semibold mb-4 text-gray-700"),
                    Div(id="query-result", cls="prose lg:prose-lg"),
                    cls="bg-white p-6 rounded-lg shadow-lg"
                ),
                Footer(
                    P("© 2024 Blue Sky Reports", cls="mb-2"),
                    P("Powered by Gemini AI", cls="text-sm text-gray-400"),
                    cls="mt-12 text-center text-gray-500 border-t pt-4"
                ),
                cls="container mx-auto px-4 py-8 max-w-4xl"
            )
        )
    )

@rt("/generate-query", methods=["POST"])
def generate_query():
    posts = read_sky_data()
    if posts:
        result = analyze_feed_topics(posts)
        return Div(
            Div(
                H3("Topics Discovered", cls="text-lg font-semibold mb-3 text-blue-800"),
                P(result, cls="text-gray-700 whitespace-pre-line"),
                cls="bg-blue-50 p-4 rounded-lg"
            )
        )
    else:
        return Div(
            Div(
                P("No data found or error accessing database", cls="text-red-600"),
                cls="bg-red-50 p-4 rounded-lg"
            )
        )
        
serve()