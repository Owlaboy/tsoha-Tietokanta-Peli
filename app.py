import random
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from secretInfo import DB_URL

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        )
    messages = result.fetchall()
    return render_template("index.html", count=len(messages), messages=messages) 

@app.route("/new")
def new():
    result = db.session.execute(text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"))
    tables = result.fetchall()
    return render_template("new.html", count=len(tables), tables=tables)

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = text("INSERT INTO messages (content) VALUES (:content)")
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")

@app.route("/result", methods=["POST"])
def result():    
    return render_template("result.html", name=request.form["tables"])

@app.route("/play")
def randRows():
    result = db.session.execute(text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"))
    tables = result.fetchall()

    result = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema' ORDER BY RANDOM() LIMIT 1;")
        )
    table_to_use = result.fetchone()[0]

    result = db.session.execute(
        text(f"SELECT * FROM {table_to_use} ORDER BY RANDOM() LIMIT 1;")
        )
    row_to_use = result.fetchone()

    result = db.session.execute(
        text(f"SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_to_use}';")
    )
    column_titles = result.fetchall()

    random_column_index = random.randint(1,len(list(column_titles))-1)    

    data_to_use=list(row_to_use)[random_column_index]

    return render_template("play.html", count=len(row_to_use), data_to_use=data_to_use, tables=tables) 
