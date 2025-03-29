# MonoDB  

**A Lightweight Key-Value Database with Web Interface and REST API**  

![License](https://img.shields.io/badge/License-MIT-blue)  
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

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

2. **Default API Key**:  
   - On first run, a `core` database is created with a default API key: `default-key`.  
   - **Change this immediately** using the `core` database commands.  

---

## Web Interface  
Access the interactive shell at `http://localhost:5000`:  
![Web Shell Demo](demo_shell.gif)
(gif incomming)

---

## API Documentation  

### Endpoint  
**`POST /api`**  
Execute database commands via HTTP.  

| Header          | Body Example      | Description                          |
|-----------------|-------------------|--------------------------------------|
| `Api-Key: KEY`  | `set user:1 John` | Requires valid API key. Plain text command. |

### Example Requests  

1. **Set a Key-Value Pair**:  
   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: default-key" -d "set book:1984 'George Orwell'"
   ```

2. **Retrieve Data**:  
   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: default-key" -d "get book:1984"
   ```

3. **Admin Command (Dump Database)**:  
   ```bash
   curl -X POST http://localhost:5000/api -H "Api-Key: default-key" -d "dump"
   ```

---

## Database Management  

### Core Database  
- Reserved for internal operations (API keys, database mappings).  
- **Do not modify manually**. Use admin commands instead.  
- Default API key: `default-key` (change with `core set db:default-key NEW_KEY`).  

### Multi-Database Support  

#### Create a New Database  
```bash
# Syntax: [core] set db:<API_KEY> <DATABASE_NAME>
core set db:my-secret-key inventory
```

#### Switch Databases in Web Shell  
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
| Command               | Description                          |
|-----------------------|--------------------------------------|
| `save`                | Force immediate data persistence.    |
| `load`                | Reload data from disk.               |
| `clear`               | Wipe all data in the current DB.     |
| `dump`                | Export all key-value pairs (JSON).   |

### Auto-Save Mechanism  
- Data is automatically saved every 5 minutes to `database.json`.  
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
└── database.json           # Auto-saved data
```

---

## License  
Distributed under the MIT License. See [LICENSE](LICENCE.txt) for details.  

---

**Contributions welcome!** Submit issues or PRs via GitHub.
