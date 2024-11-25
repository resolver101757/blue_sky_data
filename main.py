from fasthtml.common import *
import sqlite3

app, rt = fast_app()



def read_sky_data():
    """Read data from bsky_posts.db SQLite database"""
    conn = sqlite3.connect('bsky_posts.db')
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")  # Adjust table name as needed
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()
        
        

@rt("/")
def get():
    return Titled("Blue Sky Reports",
        Div(
            Button("Generate Query", 
                id="generate-query-btn",
                hx_post="/generate-query",
                hx_target="#query-result"
            ),
            Div(id="query-result")
        )
    )
    
    

@rt("/generate-query", methods=["POST"])  # Add methods=["POST"] to allow POST requests
def generate_query():
    data = read_sky_data()
    if data:
        result = "Data from database:\n" + "\n".join(str(row) for row in data)
        return P(result)
    else:
        return P("No data found or error accessing database")
    
serve()