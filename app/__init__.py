from flask import Flask, request, render_template

from app.database import Database

app = Flask(__name__)

app.secret_key = "mysecretkey"

# set data value expire
# set chave 334123 60
# set chave 334123 never
# get data


@app.route("/api/", methods=["POST"])
def api_run():
    api_key = request.headers.get("Api-Key", "")
    if api_key == "":
        return "Missing Api-Key in Header", 400

    command = request.get_data(as_text=True)
    if command == "":
        return "Missing Command in Body", 400

    db = Database()
    if api_key == app.secret_key:
        database_name = "core"
        if command == "dump":
            return db._data, 200
    else:
        success, database_name = db.run_command(f"get db:{api_key}", "core")
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
