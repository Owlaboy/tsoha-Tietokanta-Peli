from flask import redirect, render_template, request

from app import app

import random as random
from ast import literal_eval


import gameLogic
import gameData

@app.route("/")
def index():
    tables_in_db = gameData.get_tables()

    top_3_scores = gameData.get_top_user_scores()
    
    return render_template("index.html", db_tables=tables_in_db, user_scores=top_3_scores) 

@app.route("/invalid_selection")
def invalid_selection():
    return render_template("invalid_selection.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        score = int(request.form["score"])
        try:
            if request.form["replay"]:
                game_tables = literal_eval(request.form["game_tables"])
                score = -1
        except:
            pass
        if score == 0:
            game_tables = list(request.form.getlist("game_tables"))
            if len(game_tables) == 0 or len(game_tables) == 1:
                return redirect("/invalid_selection")
        elif score == -1:
            score = 0
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
    game_tables_list = literal_eval(request.form["game_tables"])
    if request.form["player_answer"] == request.form["correct_answer"]:
        return render_template("answer_correct.html", player_answer=request.form["player_answer"], correct_answer=request.form["correct_answer"],
                                score=int(request.form["score"])+1*len(game_tables_list), game_tables=request.form["game_tables"])
    else:
        return render_template("game_end.html", score=request.form["score"], correct_answer=request.form["correct_answer"] , game_tables=request.form["game_tables"])
    
@app.route("/save", methods=["POST"])
def save():
    user_name = request.form["name"]
    if len(user_name) < 3:
        return render_template("invalid_name.html", player_answer=request.form["player_answer"], correct_answer=request.form["correct_answer"],
                                score=int(request.form["score"]), game_tables=request.form["game_tables"])
    user_score = int(request.form["score"])
    gameData.insert_new_score(user_name, user_score)
    return redirect("/")


    