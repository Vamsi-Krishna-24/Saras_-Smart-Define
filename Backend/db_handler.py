import sqlite3

def execute_query(query,params=(),fetch = False):   #function FIRST
    connect = sqlite3.connect('Dictionary.db')
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
    SELECT definition, examples
    FROM dictioanry
    WHERE word = ?
    '''

    result = execute_query(query, (word,),fetch = True)

    if result:
        definition, examples, synonm = result[0]
        return{
            'word':word,
            'definition':definition,
            'examples':examples.split(','),
            'synonyms':synonm.split(',')
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