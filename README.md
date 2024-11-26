# Blue Sky Social Media Data Collector

This project is designed to collect, store, and process data from Blue Sky social media. The goal is to create a comprehensive toolset for interacting with the Blue Sky API, enabling users to gather insights and perform various operations on social media data.

## Project Structure

The main scripts you need are :

- **store_bsky_data_in_db.py**: A script to continuously collect posts from the Blue Sky timeline and store them in a SQLite database.
- **main.py**: The main application file that sets up a web interface for analyzing Blue Sky feed data using AI.
- **useful_info.md**: Contains useful links and resources for getting started with Blue Sky development.
- **.env**: Configuration file for storing environment variables and API keys.

others are just for experimenting with the data and the api:

- **scripbles.ipynb**: A Jupyter Notebook for experimenting with the Blue Sky API, testing data collection methods, and analyzing collected data.
- **get_a_list_of_posts.py**: A script to retrieve and display posts from the user's timeline.
- **post_a_message.py**: A script to post a message to Blue Sky and interact with posts (e.g., liking a post).

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/resolver101757/blue_sky_data
   cd bluesky-data-collector
   ```

2. **Install Dependencies**

   Ensure you have Python 3.12.2 or later installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Create a `.env` file in the root directory and add your credentials:

   ```
   username=your_bluesky_username
   password=your_bluesky_password
   google_api_key=your_google_api_key
   ```

4. **Run the Scripts**

   - To run the main application:
     ```bash
     python main.py
     ```

## Features

- Collect and store posts from Blue Sky in a SQLite database
- Post messages to Blue Sky
- Web interface for analyzing Blue Sky feed using AI (powered by Google's Gemini model)
- Jupyter Notebook for data exploration and experimentation

## Future Development

- Implement more advanced data processing and analysis techniques
- Enhance the web interface with more features and visualizations
- Improve error handling and logging
- Add user authentication for the web interface
- Implement real-time data streaming capabilities

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue on the GitHub repository.
