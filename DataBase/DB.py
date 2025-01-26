import sqlite3

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()

def parse("/Users/surisettivamsikrishna/Downloads/Vamsi Pc/CODES/Mark2/SARAS/Saras_-Smart-Define/DataBase/dict/data.adj",'r') as file:
    for line in file:
        if line starts with " ":
            continue
        parts = line.split("|")
        if len(parts) < 2:
            continue
        word_info=parts[0].strip()
        definition=parts[1].strip()
        example = parts[2].strip() if len(parts) > 2 else None