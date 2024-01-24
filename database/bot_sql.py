# ******************************************************************************************** #
# Every method that wants to establish a DB-Connection needs to get the db_config as parameter #
# to create the connection with 'db_conn = mysql.connector.connect(**db_config)' and           #
# a cursor with db_cursor = db_conn.cursor().                                                  #
# ******************************************************************************************** #

# ******************************************************************************************** #
# get_db_login() also reads your password for the database. If this throws an error, you might #
# need to insert your own password into 'resources/database_pw.txt'                            #
# If this file does not exist, create it.                                                      #
# ******************************************************************************************** #

# For making the import work, use: 'pip install mysql-connector-python'
import mysql.connector
# For making the import work, use: 'pip install pymysql'
import pymysql.err

# Return database login credentials
async def get_db_login():
    try:
        with open('./resources/database_pw.txt', 'r') as file:
            password = file.read()
        file.close()
    except FileNotFoundError():
        print('Could not find file with password. Please check if the following exists: \'resources/database_pw.txt\'.')

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': password,
        'database': 'leauge_insults'
    }

    return db_config

# Return a random insult for the champ that is passed as parameter
async def get_insult_from_database(db_config, champion):
    db_response = None

    try:
        db_connection = mysql.connector.connect(**db_config)
    except Exception as e:
        print('Could not establish mySQL-Connection: ' + str(e))

    try:
        cursor = db_connection.cursor(buffered=True)
    except Exception as e:
        print('Could not create cursor: ' + str(e))

    try:
        cursor.execute('''
            SELECT content
            FROM {}
            ORDER BY RAND()
            LIMIT 1
        '''.format(champion))
        db_response = cursor.fetchall()
        trimmed_db_response = db_response[0]
        double_trimmed_db_response = trimmed_db_response[0]
    except pymysql.err.ProgrammingError as e:
        if "Table" in str(e) and "doesn't exist" in str(e):
            print(f'Table for champion {champion} does not exist.')
        else:
            print('SQL-Statement failed because of ProgrammingError: ' + str(e))
    except Exception as e:
        print('SQL-Statement failed: ' + str(e))

    try:
        db_connection.close()
    except Exception as e:
        print('Could not close database-connection: ' + str(e))

    if db_response is not None:
        print("Insult:",double_trimmed_db_response)
        return str(double_trimmed_db_response)
    else:
        return db_response

# ---------------------------------------------------------------------- #
# Copyright 2024 by Sylvan013 & Anderson4366