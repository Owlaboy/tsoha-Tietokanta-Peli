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
    table_names = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        )
    tables_in_db = table_names.fetchall()

    score_search = db.session.execute(
        text("SELECT * FROM user_scores ORDER BY score DESC LIMIT(3)")
    )
    top_3_scores = score_search.fetchall()

    return render_template("index.html", db_tables=tables_in_db, user_scores=top_3_scores) 

@app.route("/play", methods=["GET", "POST"])
def randRows():
    if request.method == "POST":
        score = int(request.form["score"])
    
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


    return render_template("play.html", count=len(row_to_use), data_to_use=data_to_use, tables=tables, correct_answer=table_to_use, score=score) 


@app.route("/result", methods=["POST"])
def result():
    if request.form["tables"] == request.form["correct_answer"]:
        return render_template("answer_correct.html", name=request.form["tables"], correct_answer=request.form["correct_answer"], score=int(request.form["score"])+1)
    else:
        return render_template("game_end.html", score=request.form["score"])
    
@app.route("/save", methods=["POST"])
def save():
    user_name = request.form["name"]
    user_score = int(request.form["score"])
    sql = text("INSERT INTO user_scores (player_name, score) VALUES (:player_name, :score)")
    db.session.execute(sql, {"player_name":user_name, "score":user_score})
    db.session.commit()
    return redirect("/")

    