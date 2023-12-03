import random as random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from db import db


def get_tables():
    table_names = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        )
    tables_in_db = table_names.fetchall()

    return tables_in_db

def get_random_table():
    result = db.session.execute(
        text("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema' ORDER BY RANDOM() LIMIT 1;")
        )
    random_table = result.fetchone()[0]

    return random_table

def get_random_row(table):
    result = db.session.execute(
        text(f"SELECT * FROM {table} ORDER BY RANDOM() LIMIT 1;")
        )
    random_row = result.fetchone()

    return random_row

def get_column_titles(table):
    result = db.session.execute(
        text(f"SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}';")
    )
    column_titles = result.fetchall()

    return column_titles

def get_column_titles_type_text(table):
    result = db.session.execute(
        text(f"SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}' AND DATA_TYPE = 'text';")
    )
    column_titles = result.fetchall()

    return column_titles

def get_random_row(table):
    result = db.session.execute(
        text(f"SELECT * FROM {table} ORDER BY RANDOM() LIMIT 1;")
        )
    random_row = result.fetchone()

    return random_row

def get_random_column_index(column_titles):
    random_column_index = random.randint(0,len(list(column_titles))-1)    

    return random_column_index

def get_data_to_use(random_row, random_column_index):
    data_to_use=list(random_row)[random_column_index]

    return data_to_use

def easy_mode(tables):
    random_table = random.choice(tables)
    random_row = get_random_row(random_table)
    column_titles = get_column_titles_type_text(random_table)
    random_column_index = get_random_column_index(column_titles)
    data_to_use = get_data_to_use(random_row, random_column_index)

    return random_row, data_to_use, tables, random_table
