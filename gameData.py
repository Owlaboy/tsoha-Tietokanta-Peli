import random as random
from sqlalchemy.sql import text

from db import db


def get_tables():
    table_names = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        )
    tables_in_db = table_names.fetchall()

    return tables_in_db


def get_user_scores():
    score_search = db.session.execute(
        text("SELECT * FROM user_scores ORDER BY score DESC LIMIT(3)")
    )
    top_3_scores = score_search.fetchall()

    return top_3_scores

def insert_new_score(user_name, user_score):
    sql = text("INSERT INTO user_scores (player_name, score) VALUES (:player_name, :score)")
    db.session.execute(sql, {"player_name":user_name, "score":user_score})
    db.session.commit()