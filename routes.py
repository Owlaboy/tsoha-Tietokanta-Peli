from flask import redirect, render_template, request

from app import app

import random as random
from ast import literal_eval


import gameLogic
import gameData

@app.route("/")
def index():
    tables_in_db = gameData.get_tables()

    top_3_scores = gameData.get_user_scores()

    return render_template("index.html", db_tables=tables_in_db, user_scores=top_3_scores) 

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        score = int(request.form["score"])
        print(request.form["game_tables"])
        print(random.choice(list(request.form["game_tables"])))
        if score == 0:
            game_tables = list(request.form.getlist("game_tables"))
        else:
            game_tables = literal_eval(request.form["game_tables"])
        
    game_data = gameLogic.easy_mode(game_tables)


    row_to_use = game_data[0]
    data_to_use = game_data[1]
    game_tables = game_data[2]
    table_to_use = game_data[3]


    return render_template("play.html", data_to_use=data_to_use, game_tables=game_tables, correct_answer=table_to_use, score=score) 

@app.route("/result", methods=["POST"])
def result():
    if request.form["tables"] == request.form["correct_answer"]:
        return render_template("answer_correct.html", name=request.form["tables"], correct_answer=request.form["correct_answer"],
                                score=int(request.form["score"])+1, game_tables=request.form["game_tables"])
    else:
        return render_template("game_end.html", score=request.form["score"], correct_answer=request.form["correct_answer"])
    
@app.route("/save", methods=["POST"])
def save():
    user_name = request.form["name"]
    user_score = int(request.form["score"])
    gameData.insert_new_score(user_name, user_score)
    return redirect("/")

    