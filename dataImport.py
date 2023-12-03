#make a for loop that goes over all the files in the directory
#and imports them into the database
#also make a function that imports a single file
#and a function that imports all files
#also make a function that imports a single file and returns the dataframe

import pandas as pd
import glob
import numpy as np
from sqlalchemy import create_engine

from secretInfo import DB_URL

engine = create_engine(DB_URL)

def import_single_file(file_path):
    df = pd.read_csv(file_path)
    df = df.replace(np.nan, '', regex=True)
    df.to_sql(file_path.split("/")[-1].split(".")[0], engine, if_exists="replace")
    return df

def import_all_files():
    for file in glob.glob("GameData/*.csv"):
        import_single_file(file)


if __name__ == "__main__":
    import_all_files()