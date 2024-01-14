import operation_for_db

class User:

    def __init__(self, login):

        self.cur_user = None
        self.user_login = login

    def user_f_name(self):
        self.cur_user = operation_for_db.SQLiteDB('f_user_name',
                                              'users',
                                              f'',
                                              f'',
                                              f'{self.user_login}',
                                              f'',
                                              f'',
                                              f'')
        return self.cur_user.select()

    def user_l_name(self):
        self.cur_user = operation_for_db.SQLiteDB('l_user_name',
                                              'users',
                                              f'',
                                              f'',
                                              f'{self.user_login}',
                                              f'',
                                              f'',
                                              f'')
        return self.cur_user.select()

    def user_email(self):
        self.cur_user = operation_for_db.SQLiteDB('user_email',
                                              'users',
                                              f'',
                                              f'',
                                              f'{self.user_login}',
                                              f'',
                                              f'',
                                              f'')
        return self.cur_user.select()

    def delete_current_user(self):
        self.cur_user = operation_for_db.SQLiteDB('*',
                                              'users',
                                              f'',
                                              f'',
                                              f'{self.user_login}',
                                              f'',
                                              f'',
                                              f'')
        return self.cur_user.delete()
