# Blue Sky Social Media Data Collector

This project is designed to collect, store, and process data from Blue Sky social media. The goal is to create a comprehensive toolset for interacting with the Blue Sky API, enabling users to gather insights and perform various operations on social media data.

## Project Structure

- **scripbles.ipynb**: A Jupyter Notebook for experimenting with the Blue Sky API and testing data collection methods.
- **get_a_list_of_posts.py**: A script to retrieve and display posts from the user's timeline.
- **post_a_message.py**: A script to post a message to Blue Sky and interact with posts (e.g., liking a post).

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/bluesky-data-collector.git
   cd bluesky-data-collector
   ```

2. **Install Dependencies**

   Ensure you have Python 3.12.2 or later installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Create a `.env` file in the root directory and add your Blue Sky credentials:

   ```
   username=your_username
   password=your_password
   ```

4. **Run the Scripts**

   - To get a list of posts, run:

     ```bash
     python get_a_list_of_posts.py
     ```

   - To post a message, run:

     ```bash
     python post_a_message.py
     ```

## Future Development

- **Data Storage**: Implement a database to store collected data for further analysis.
- **Data Processing**: Develop scripts to process and analyze the collected data.
- **Enhanced API Interaction**: Add more features to interact with the Blue Sky API, such as commenting, sharing, and following users.
- **Error Handling**: Improve error handling and logging for more robust scripts.
- **User Interface**: Create a user-friendly interface for non-technical users to interact with the tool.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact [your email](mailto:your.email@example.com).
