
# MonoDB

MonoDB is a simple key-value database with a web-based shell interface. It is built using Flask and provides a RESTful API for interacting with the database.

## Objective

The objective of this system is to serve as an easy-to-use and modify local database, primarily intended for use in internal company tools. It is secure and very easy to integrate.

## Features

- Key-value storage
- Web-based shell interface
- RESTful API for database operations
- Auto-save functionality

## Project Structure

```
MonoDB/
├── .gitignore
├── .replit
├── LICENCE.txt
├── poetry.lock
├── pyproject.toml
├── readme.md
├── run.py
├── wsgi.py
└── app/
    ├── __init__.py
    ├── __main__.py
    ├── database.py
    └── templates/
        └── shell.html
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/monodb.git
    cd monodb
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

3. Set the `SECRET_KEY` environment variable:
    ```sh
    export SECRET_KEY='your_secret_key'
    ```

## Usage

### Running the Application

To run the application locally, use the following command:
```sh
python run.py # it get app and run port 5000 (debug)
```
Or
```sh
python3 -m app # it run port 8080 app/__main__.py (sim-productio)
```

The application will be available at `http://localhost:5000`.

### Deployment

To deploy the application using Gunicorn, use the following command:
```sh
gunicorn -w 4 -b 0.0.0.0:8080 app:create_app()
```

### API Endpoints

- `POST /api`: Execute a command on the database.
    - Headers:
        - `Api-Key`: Your API key.

    Request Parts
    | Part    | Value          | Explain                                                                 |
    |---------|----------------|-------------------------------------------------------------------------|
    | URL     | /api           | The endpoint to which the request is sent.                              |
    | Method  | POST           | The HTTP method used for the request.                                   |
    | Header Api-Key | your_api_key   | Metadata for the request, such as `Api-Key` for authentication.         |
    | Body    | set key value  | The data sent with the request, typically in plain text for key-value API commands. |

### Example cURL Requests

To interact with the API, you can use the following cURL commands:

1. Set a key-value pair:
    ```sh
    curl -X POST http://localhost:5000/api -H "Api-Key: your_api_key" -d "set key value"
    ```

2. Get the value of a key:
    ```sh
    curl -X POST http://localhost:5000/api -H "Api-Key: your_api_key" -d "get key"
    ```

3. Delete a key:
    ```sh
    curl -X POST http://localhost:5000/api -H "Api-Key: your_api_key" -d "del key"
    ```

4. Get all data:
    ```sh
    curl -X POST http://localhost:5000/api -H "Api-Key: your_api_key" -d "getalldata"
    ```

### Web Interface

The web-based shell interface is available at the root URL (`/`). It allows you to enter commands and view the output directly in your browser.

## Database Commands

- `set key value`: Set a key-value pair.
- `get key`: Get the value of a key.
- `del key`: Delete a key.
- `help`: Display available commands.
- `getalldata`: Get all data in the selected database.

### Admin Commands

- `dump`: Dump all data in the database.
- `save`: Save the current state of the database.
- `load`: Load the database from the saved state.
- `clear`: Clear all data in the database.

## How the Database Works

Under the hood, MonoDB uses a simple dictionary to store key-value pairs in memory. The `database.py` module handles all database operations, including setting, getting, and deleting keys. The auto-save functionality ensures that the database state is periodically saved to a file, allowing for data persistence across application restarts.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENCE.txt) file for details.

