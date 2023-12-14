import random as random
from sqlalchemy.sql import text

from db import db


def get_tables():
    table_names = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        )
    tables_in_db = table_names.fetchall()

    return tables_in_db


def get_top_user_scores():
    score_search = db.session.execute(
        text("""
             SELECT player_name, score, (
                SELECT COUNT(*) FROM user_scores WHERE user_scores.player_name = u.player_name
             ) AS play_count 
             FROM user_scores u 
             ORDER BY score 
             DESC LIMIT 3
             """)
             )
    
    top_3_scores = score_search.fetchall()

    return top_3_scores

def get_play_count(player_name):
    sql = text("SELECT count(*) FROM user_scores WHERE player_name = :player_name")
    play_count = db.session.execute(sql, {"player_name":player_name})
    play_count = play_count.fetchone()

    return play_count

def insert_new_score(player_name, user_score):
    sql = text("INSERT INTO user_scores (player_name, score) VALUES (:player_name, :score)")
    db.session.execute(sql, {"player_name":player_name, "score":user_score})
    db.session.commit()