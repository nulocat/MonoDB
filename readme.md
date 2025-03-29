# MonoDB

**A Lightweight Key-Value Database with Web Interface and REST API**

![License](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-green)

A simple NoSQL database designed for internal tools, featuring a web-based shell and RESTful API. Built with Flask for easy integration and extensibility.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Web Interface](#web-interface)
- [API Documentation](#api-documentation)
- [Database Management](#database-management)
  - [Core Database](#core-database)
  - [Multi-Database Support](#multi-database-support)
- [Advanced Usage](#advanced-usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features

- 🚀 **Key-Value Storage**: Simple `set`, `get`, and `del` operations.
- 🌐 **Web-Based Shell**: Interactive browser interface for direct database access.
- 🔒 **API Key Authentication**: Secure endpoints with customizable keys.
- 💾 **Auto-Save & Persistence**: Data preserved across restarts.
- 🛠 **Admin Tools**: Multi-database management, backups, and bulk operations.
- 📦 **Lightweight**: Single-file storage with minimal dependencies.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/monodb.git
   cd monodb
   ```

2. **Install Dependencies (via Poetry)**:

   ```bash
   poetry install
   ```

---

## Quick Start

### Running the Server

**Development Mode (Port 5000)**:

```bash
python run.py  # Debug mode with hot reload
```

**Production Mode (Port 8080)**:

```bash
python3 -m app  # Simulated production environment
```

### Deployment with Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8080 app:create_app()
```

---

## Configuration

1. **Set the Secret Key**:

   ```bash
   export SECRET_KEY='your_random_secret_here'
   ```

2. **Admin Api\_Key**:

- The Admin API Key is derived from the server's SECRET\_KEY. When the server starts, it reads the SECRET\_KEY environment variable and uses it to authenticate administrative actions. Any request using this key is granted full admin privileges.

---

## Web Interface

Access the interactive shell at `http://localhost:5000`:\


(gif incomming)

---

## API Documentation

### Endpoint

**`POST /api`**\
Execute database commands via HTTP.

| Header         | Body Example      | Description                                 |
| -------------- | ----------------- | ------------------------------------------- |
| `Api-Key: KEY` | `set user:1 John` | Requires valid API key. Plain text command. |

### Example Requests

1. **Update an Existing Key**:

   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: your_secret_key" -d "set user:1234 'John Doe, jonhdoe@corp.com'"
   ```

2. **Get a Key**:

   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: your_secret_key" -d "get user:1234"
   ```

3. **Delete a Key**:

   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: your_secret_key" -d "del user:1234"
   ```

4. **Admin Command (Clear Database)**:

   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: your_secret_key" -d "clear"
   ```

---

## Database Management

### Commands

- `set <key> <value>`: Set a key-value pair.
- `get <key>`: Get the value of a key.
- `del <key>`: Delete a key.
- `help`: Display available commands.
- `getalldata`: Get all data in the selected database.

### Core Database

- Reserved for internal operations (API keys, database mappings).
- **Do not modify manually**. Use admin commands instead.
- The Admin Api-Key is the app's secret key, and with it, you can execute all admin commands.

### Multi-Database Support

#### Create a New Database

```bash
# Syntax: [core] set db:<API_KEY> <DATABASE_NAME>
core set db:invetory_api_key inventory
```

#### Switch Databases in Web Shell (has admin api\_key)

```bash
# Prefix commands with the database name:
inventory set item:1 "Product A"
```

#### List All Databases

```bash
core getalldata  # Returns all API key-database mappings
```

---

## Advanced Usage

### Admin Commands

| Command                   | Description                          |
| ------------------------- | ------------------------------------ |
| `save`                    | Force immediate data persistence.    |
| `load`                    | Reload data from disk.               |
| `clear`                   | Wipe all data in the current DB.     |
| `dump`                    | Export all key-value pairs (JSON).   |
| `<database> <db_command>` | Run a command in a selected database |

### Auto-Save Mechanism

- MonoDB **is not based on JSON files** but rather a **Python dictionary stored in memory**. JSON is only used as a means to ensure data persistence in case of shutdown.  
- Disk storage occurs **only periodically**, ensuring better performance during normal operations.  
- Manual saves: `curl -X POST ... -d "save"`

---

## Project Structure

```
MonoDB/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── database.py         # Core database logic
│   └── templates/shell.html  # Web interface
├── run.py                  # Development launcher
├── wsgi.py                 # Production WSGI entry
└── database.json           # Auto-saved data (backup)
```

---

## License

Distributed under the MIT License. See [LICENSE](LICENCE.txt) for details.

---

**Contributions welcome!** Submit issues or PRs via GitHub.

