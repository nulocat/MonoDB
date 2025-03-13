from flask import Flask, request, render_template

from app.database import Database

import os
import secrets


def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get('SECRET_KEY', secrets.token_urlsafe(32))

    @app.route("/api", methods=["POST"])
    def api_run():
        api_key = request.headers.get("Api-Key", "")
        if api_key == "":
            return "Missing Api-Key in Header", 400

        command = request.get_data(as_text=True)
        if command == "":
            return "Missing Command in Body", 400

        db = Database()
        if api_key == app.secret_key:
            status, result = db.run_admin_command(command)
        else:
            success, database_name = db.run_command(f"get db:{api_key}",
                                                    "core")
            if not success:
                return "Invalid Api-Key", 400

            status, result = db.run_command(command, database_name)

        if status:
            return result, 200
        else:
            return result, 400

    @app.route("/", methods=["GET"])
    def index():
        return render_template("shell.html")

    return app
