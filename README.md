# Subsidiary Finder

Subsidiary Finder is a Python application that allows users to search for subsidiaries of a company and store the results in a SQLite database.

## Features

- **Search Subsidiaries**: Users can enter the name of a company and search for its subsidiaries.
- **Database Storage**: Subsidiary names found during the search are stored in a SQLite database to maintain a record of the data.
- **Normalization**: Subsidiary names are normalized using a set of rules to ensure consistency and accuracy.
- **Streamlit Interface**: The application uses Streamlit to provide a user-friendly interface for searching and viewing subsidiary data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/subsidiary-finder.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the ChromeDriver executable and place it in the `chromedriver-win32` directory.

## Usage

1. Run the `main.py` file:

    ```bash
    streamlit run main.py
    ```

2. Enter the name of the company you want to search for subsidiaries.
3. Click the "Search" button to initiate the search.
4. View the list of subsidiaries in the table.
5. Subsidiary names will be stored in the database automatically.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
