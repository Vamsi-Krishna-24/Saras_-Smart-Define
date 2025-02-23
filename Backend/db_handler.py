import sqlite3
import os

def execute_query(query,params=(),fetch = False):   #function FIRST
    connect = sqlite3.connect('/Users/surisettivamsikrishna/Downloads/Vamsi Pc/CODES/Mark2/SARAS/Saras_-Smart-Define/DataBase/Dictionary.db')
    cursor = connect.cursor()
    cursor.execute(query,params)

    if fetch:
        result = cursor.fetchall()
        connect.close()
        return result
    
    connect.commit()
    connect.close()


def get_word_meaning(word):                         #Function SECOND
    query='''
    SELECT definition, examples, synonm
    FROM dictionary
    WHERE word1 = ?
    '''

    result = execute_query(query, (word,),fetch = True)

    if result:
        definition, examples, synonm = result[0]
        return{
            'word':word,
            'definition':definition,
            'examples':examples.split(',') if examples else [],
            'synonyms':synonm.split(',') if synonm else []
        }
    else:
        return None



def insert_word(word1,synonm,definition,examples):          #THIRD Function 
    query = '''
    INSERT INTO dictionary(word1,synonm,definition,examples)
    VALUES (?,?,?,?)
    '''

    synonm_str = ','.join(synonm) if synonm else ''
    example_str = ','.join(examples) if examples else ''

    execute_query(query, (word1,synonm_str,definition,example_str))

    #DB have been designed and functioned properly till now.


print(os.path.abspath('Dictionary.db'))