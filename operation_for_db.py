import sqlite3
import date_time_module


# потім зроблю, щоб в налаштуваннях цей шлях можна було б побачити
def path_to_db():
    path = 'data/osbb.db'
    return path


class SQLiteDB:

    user_password: str

    def __init__(self, select_obj, table_name, f_user_name, l_user_name, user_login, user_password, user_email, user_role):
        self.connection = sqlite3.connect(f'{path_to_db()}')
        self.cursor = self.connection.cursor()
        self.select_obj = select_obj
        self.table_name = table_name
        self.f_user_name = f_user_name
        self.l_user_name = l_user_name
        self.user_login = user_login
        self.user_password = user_password
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

    def select(self):
        query = (f'SELECT {self.select_obj} '
                 f'FROM {self.table_name} '
                 f'WHERE user_login = "{self.user_login}"')
        self.execute(query)
        return self

    def insert_user(self):
        query = (f'INSERT INTO users '
                 f'(f_user_name, l_user_name, user_login, user_password, user_email, user_role, create_data) '
                 f'VALUES '
                 f'("{self.f_user_name}", "{self.l_user_name}", "{self.user_login}", "{self.user_password}", "{self.user_email}", "{self.user_role}", {date_time_module.date_time_to_unix()})')
        self.execute(query)
        self.commit()

    def update(self, column, new_value):
        query = (f'UPDATE {self.table_name} '
                 f'SET {column} = {new_value} '
                 f'WHERE user_login = "{self.user_login}"')
        self.execute(query)
        self.commit()

    def delete(self):
        query = (f'DELETE FROM {self.table_name} '
                 f'WHERE user_login = "{self.user_login}"')
        self.execute(query)
        self.commit()
