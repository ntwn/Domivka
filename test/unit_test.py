import sqlite3


def units():
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * '
                   f'FROM units')
    cur = cursor.fetchall()
    connection.close()
    return cur


for unit in units():

    print(f'{unit[0]}: {unit[1]}')
