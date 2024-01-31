# В майбутньому реалізую сповіщення на пошту і увімкну для перевірки
# import email_validator

import operation_for_db


class Auth:

    def __init__(self, user_login, user_password, user_confirm_password=" ", f_user_name=" ", l_user_name=" ",  user_email=" ", user_role='user'):
        self.user_data = None
        self.hash_pass_digest = ''
        self.hash_pass_object = ''
        self.f_user_name = f_user_name
        self.l_user_name = l_user_name
        self.user_login = user_login
        self.user_password = user_password
        self.user_confirm_password = (user_confirm_password or ' ')
        self.user_email = user_email
        self.user_role = user_role
        self.user = operation_for_db.SQLiteDBUser(f'{self.f_user_name}',
                                                  f'{self.l_user_name}',
                                                  f'{self.user_login}',
                                                  f'{self.user_password}',
                                                  f'{self.user_email}',
                                                  f'{self.user_role}')

    def register(self):
        self.user.select_user()
        self.user_data = self.user.fetchone()
        if len(self.user_login) < 3:
            return 'chip_login'
        elif self.user_data is not None:
            if self.user_login in self.user_data:
                return 'login_exists'
        elif len(self.user_password) < 3:
            return 'chip_password'
        elif self.user_password != self.user_confirm_password:
            return 'wrong_confirm_password'

        # В майбутньому реалізую сповіщення на пошту і увімкну цю перевірку
        #
        # elif self.user_email == self.user_data[3]:
        #     return 'email_exists'
        # elif email_validator.validate_email(self.user_email):
        #     return 'email_not_valid'

        else:
            return self.user_password
            # self.user_registration = operation_for_db.SQLiteDBUser('*',
            #                                   'users',
            #                                   f'{self.f_user_name}',
            #                                   f'{self.l_user_name}',
            #                                   f'{self.user_login}',
            #                                   f'{self.hash_password()}',
            #                                   f'{self.user_email}',
            #                                   f'{self.user_role}')
            # self.user_registration.insert_user()
            # return True

    def login(self):
        self.user.select_user()
        self.user_data = self.user.fetchone()
        # Перевіряємо, чи існує користувач з таким ім'ям
        if not self.user_data:
            return 'user_not_found'
        elif self.user_password not in self.user_data:
            return 'password_not_valid'
        else:
            return self.user_data
