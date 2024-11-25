from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Blue Sky Reports",
        Div(
            Button("Generate Query", id="generate-query-btn"),
            Div(id="query-result")
        )
    )

@rt("/generate-query")
def post():
    # This is where you'd implement the query generation logic
    generated_query = "SELECT * FROM sky_data WHERE color = 'blue';"
    return P(generated_query)

serve()