import operation_for_db


class User:

    def __init__(self, login):
        self.cur_user = None
        self.user_login = login

    def user_f_name(self):
        self.cur_user = operation_for_db.SQLiteDBUser('f_user_name',
                                                  f'',
                                                  f'{self.user_login}',
                                                  f'',
                                                  f'',
                                                  f'')
        return self.cur_user.select_user()

    def user_l_name(self):
        self.cur_user = operation_for_db.SQLiteDBUser('l_user_name',
                                                  f'',
                                                  f'{self.user_login}',
                                                  f'',
                                                  f'',
                                                  f'')
        return self.cur_user.select_user()

    def user_email(self):
        self.cur_user = operation_for_db.SQLiteDBUser('user_email',
                                                  f'',
                                                  f'{self.user_login}',
                                                  f'',
                                                  f'',
                                                  f'')
        return self.cur_user.select_user()

    def delete_current_user(self):
        self.cur_user = operation_for_db.SQLiteDBUser('*',
                                                  f'',
                                                  f'{self.user_login}',
                                                  f'',
                                                  f'',
                                                  f'')
        return self.cur_user.delete_user()
