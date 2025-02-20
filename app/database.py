import os
import json
import threading
from typing import Dict, Tuple
import logging


class Database:
    _instance = None
    _save_interval = 60  # 1 minuto
    _save_thread: threading.Timer | None = None
    _db_file = "db/main.json"

    _data: Dict[str, Dict[str, str]] = {}  # Data {database_name: {key: value}}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._data = {}
            cls._instance.load()  # Carrega os dados ao iniciar
            cls._instance._start_auto_save()
        return cls._instance

    def _start_auto_save(self):
        self._save_thread = threading.Timer(self._save_interval,
                                            self._auto_save)
        self._save_thread.start()

    def _auto_save(self):
        self.save()
        self._start_auto_save()

    def save(self):
        os.makedirs(os.path.dirname(self._db_file), exist_ok=True)
        with open(self._db_file, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=4)

    def load(self):
        if os.path.exists(self._db_file):
            with open(self._db_file, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self._data = data
                    logging.info("DB: LOAD DONE")
                except Exception as e:
                    logging.error("DB: LOAD FAILED")
                    logging.error(f"DB: ERROR OUTPUT:\n{e}")

    def run_command(self, command: str, database: str) -> Tuple[bool, str]:
        try:
            if database not in self._data:
                self._data[database] = {}

            split = command.split(" ")
            match split[0].lower():
                case "set":
                    key = split[1]
                    value = split[2]
                    self._data[database][key] = value
                    return True, "Written"
                case "get":
                    key = split[1]
                    return True, self._data[database][key]
                case "del":
                    key = split[1]
                    del self._data[database][key]
                    return True, "Deleted"
                case "help":
                    return True, "Available commands:\nset key value\nget key\ndel key\nhelp\ngetalldata"
                case "getalldata": # be like admin dump but only in database selected
                    return True, json.dumps(self._data[database], indent=4)
                case _:
                    return False, "COMMAND NOT FOUND"

        except:
            return False, "COMMAND DUMPED, CHECK YOUR COMMAND"

    def run_admin_command(self, command: str) -> Tuple[bool, str]:
        try:
            split = command.split(" ")
            database = split.pop(0) or "core"
            command = " ".join(split)
            
            
            return self.run_command(command, database)
        except:
            return False, "ADMIN COMMAND DUMPED, CHECK YOUR COMMAND"
            
