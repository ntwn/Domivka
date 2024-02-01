import sqlite3
import date_time_module


# потім зроблю, щоб в налаштуваннях цей шлях можна було б побачити
def path_to_db(path='data/database.db'):
    # path = 'data/database.db'
    return path


class SQLiteDBUser:
    user_password: str

    def __init__(self, f_user_name, l_user_name, user_login, user_password, user_email, user_role,
                 path_todb=f'{path_to_db()}'):
        self.path_to_db = path_todb
        self.connection = sqlite3.connect(f'{self.path_to_db}')
        self.cursor = self.connection.cursor()
        self.f_user_name = f_user_name
        self.l_user_name = l_user_name
        self.__user_login = user_login
        self.__user_password = user_password
        self.user_email = user_email
        self.user_role = user_role

    def __del__(self):
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    # робота з користувачем
    def select_user(self):
        query = (f'SELECT * '
                 f'FROM users '
                 f'WHERE user_login = "{self.__user_login}"')
        self.execute(query)
        return self

    def insert_user(self):
        query = (f'INSERT INTO users '
                 f'(f_user_name, l_user_name, user_login, user_password, user_email, user_role, create_data) '
                 f'VALUES '
                 f'("{self.f_user_name}",'
                 f' "{self.l_user_name}",'
                 f' "{self.__user_login}",'
                 f' "{self.__user_password}",'
                 f' "{self.user_email}",'
                 f' "{self.user_role}",'
                 f' {date_time_module.date_time_to_unix()})')
        self.execute(query)
        self.commit()

    def update_user(self, column, new_value):
        query = (f'UPDATE users '
                 f'SET {column} = {new_value} '
                 f'WHERE user_login = "{self.__user_login}"')
        self.execute(query)
        self.commit()

    def delete_user(self):
        query = (f'DELETE FROM users '
                 f'WHERE user_login = "{self.__user_login}"')
        self.execute(query)
        self.commit()


class SQLiteDBPerson:

    def __init__(self, person_id, number_of_apartment, street, city, path_todb=f'{path_to_db()}'):
        self.path_to_db = path_todb
        self.connection = sqlite3.connect(f'{self.path_to_db}')
        self.cursor = self.connection.cursor()
        self.number_of_apartment = number_of_apartment
        self.street = street
        self.city = city
        self.person_id = person_id

    def __del__(self):
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def select_area(self):
        query = (f'SELECT person.* '
                 f'FROM apartment '
                 f'INNER JOIN person '
                 f'ON apartment.number_of_apartment = person.number_of_apartment '
                 f'WHERE '
                 f'person.number_of_apartment == {self.number_of_apartment} AND '
                 f'apartment.street == {self.street} AND '
                 f'apartment.city == {self.city}')
        self.execute(query)
        return self

    def select_appartment_count(self):
        query = (f'SELECT COUNT(*) '
                 f'FROM apartment '
                 f'WHERE street = {self.street} AND city = {self.city}')
        self.execute(query)
        return self

    def select_vote_yes(self):
        query = (f'SELECT * '  # vote_for_questions.vote as vote '
                 f'FROM person '
                 f'INNER JOIN vote_for_questions '
                 f'ON vote_for_questions.id_person = person.id '
                 f'WHERE person.id = {self.person_id} AND vote_for_questions.vote = 1 ')
        self.execute(query)
        return self

    def select_vote_no(self):
        query = (f'SELECT * '  # vote_for_questions.vote as vote '
                 f'FROM person '
                 f'INNER JOIN vote_for_questions '
                 f'ON vote_for_questions.id_person = person.id '
                 f'WHERE person.id = {self.person_id} AND vote_for_questions.vote = 0 ')
        self.execute(query)
        return self

    def insert_user(self):
        query = (f'INSERT INTO ??? '
                 f'(???) '
                 f'VALUES '
                 f'(???)')
        self.execute(query)
        self.commit()

    def update_user(self):
        query = (f'UPDATE ??? '
                 f'SET ??? = ??? '
                 f'WHERE ???')
        self.execute(query)
        self.commit()

    def delete_user(self):
        query = (f'DELETE FROM ??? '
                 f'WHERE ???')
        self.execute(query)
        self.commit()


class SQLiteDBUnits:
    def __init__(self, name_unit=None, number=None, street=None, city=None, path_todb=f'{path_to_db()}'):
        self.path_to_db = path_todb
        self.connection = sqlite3.connect(f'{self.path_to_db}')
        self.cursor = self.connection.cursor()
        self.name_unit = name_unit
        self.number = number
        self.street = street
        self.city = city

    def __del__(self):
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def select_units(self):
        query = (f'SELECT * '
                 f'FROM units')
        self.execute(query)
        return self

    def insert_unit(self):
        query = (f'INSERT INTO units '
                 f'(name_unit, number, street, city) '
                 f'VALUES '
                 f'("{self.name_unit}",'
                 f' "{self.number}",'
                 f' "{self.street}",'
                 f' "{self.city}"')
        self.execute(query)
        self.commit()

    def update_unit(self, name_unit, column, new_value):
        query = (f'UPDATE units '
                 f'SET {column} = {new_value} '
                 f'WHERE name_unit = "{name_unit}"')
        self.execute(query)
        self.commit()

    def delete_delete(self):
        query = (f'DELETE FROM users '
                 f'WHERE user_login = "{self.name_unit}"')
        self.execute(query)
        self.commit()


