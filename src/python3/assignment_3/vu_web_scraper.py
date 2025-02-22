import os 
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup

# open & retrieve list of html files
sub_dir = r"/Users/lukasvm/UTK /Spring 25/DATA 304/data_wrangling_304/data/assignment_1/raw/class_submissions/"
webpages = []

for name in os.listdir(sub_dir):
    if name.endswith('.html'):
        webpages.append(name)

webpages = [os.path.join(sub_dir, file_name) for file_name in webpages]

# open each file & scrape data
database = []
for page in webpages:
    with open(page, 'r') as webpage:
        soup = BeautifulSoup(webpage, 'html.parser')
        # find name
        name = soup.find('h1')

        # find table of interests
        table = soup.find('table')
            # extract all favs from table rows 
        favs = []
        for row in table.children:
            favs.append(row.get_text())
            
            # clean favs array
        favs = favs[3::2] # get valuable strings
        for i in range(len(favs)):
            favs[i] = favs[i].strip('\n!').split('\n')
            favs[i].append(name.get_text())

        # save to temporary database
        database.append(favs)
# print(database)

# connect to database
path_to_db = r'/Users/lukasvm/UTK /Spring 25/DATA 304/data_wrangling_304/data/assignment_3/parsed_bios.sqllite'


def create_tables(cursor):
    create_table1 = """
    CREATE TABLE IF NOT EXISTS
    names(
        name_id INTEGER PRIMARY KEY,
        name TEXT
    )"""
    create_table2 = """
    CREATE TABLE IF NOT EXISTS
    favorites(
        favorite_id INTEGER PRIMARY KEY,
        name_id INTEGER,
        category TEXT,
        favorite TEXT,
        FOREIGN KEY(name_id) REFERENCES names(name_id)
    )
    """
    cursor.execute(create_table1)
    cursor.execute(create_table2)
    print('tables created!')



    #  Insert values to table : names
def insert_names(path, names):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    sql_insert_names = """
    INSERT INTO names(name)
    VALUES 
    """
    for i, person in enumerate(names):
        name = person[0][2]
        sql_insert_names += f'\n\t("{name}")'
        if i != len(database) -1:
            sql_insert_names += ','

    cursor.execute(sql_insert_names)
    connection.commit()
    connection.close()

def fetch_data(path, query):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()    
    res = cursor.execute(query)
    res =  res.fetchall()
    connection.close()
    return res


def insert_favs(path, favs):
    connection = sqlite3.connect(path)
    cursor = connection.cursor() 
    sql_insert_favs = f"""
            INSERT INTO favorites(name_id, category, favorite)
            VALUES 
        """  
    for person in favs:
        name = person[0][2]
        res = cursor.execute(f"""
                       SELECT name_id 
                       FROM names 
                       WHERE name = '{name}'""")
        id = res.fetchone()[0]
        for row in person:
            cat, fav, n = row
            sql_insert_favs += f"({id}, '{cat}', '{fav}' ),\n"
        
    sql_insert_favs  = sql_insert_favs[:-2]

    cursor.execute(sql_insert_favs)
    connection.commit()
    connection.close()
    
# create_tables(cursor)
# insert_names(path_to_db, database)
# insert_favs(path_to_db, database)

# test
test_query = """
    SELECT *
    FROM favorites
    LEFT JOIN names
    ON favorites.name_id = names.name_id
"""
data = fetch_data(path_to_db, test_query)
print(data)