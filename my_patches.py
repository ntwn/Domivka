import string
import hashlib

import main
from UI.login_window_ui import Ui_LoginWindow

# не допускає, некоректноє інпута в поле input (ТРЕБА ПОЯСНИТИ ТОЧНІШЕ)
# певно вона піде під видалення


def coalesce(*args):
    for arg in args:
        if arg != '' and arg is not None:
            return arg
    return None

# перевіряє рівень пароля (з тестами в папці test)


def password_strange(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'

    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    special = string.punctuation
    counts = 0

    for symbols in (digits, uppers, lowers, special):
        if any(e in symbols for e in value):
            counts += 1
            continue

    if counts == 4:
        return 'Super Very Good'
    if counts == 3:
        return 'Very Good'
    return 'Weak' if counts == 1 else 'Good'


def set_lang(lang):
    if lang == 'EN':
        main.LoginWindow().ui.change_on_enter_button.setText('Enter')
        print(main.LoginWindow().ui.change_on_enter_button.text())
        main.LoginWindow().ui.login_input.setText('Login')
        print(f'Set {lang}')
        return lang


# хеширує пароль і повертає хеш-суму
def hash_password(user_password):
    hash_pass_object = hashlib.md5()
    hash_pass_object.update(user_password.encode('utf-8'))
    hash_pass_digest = hash_pass_object.hexdigest()
    return hash_pass_digest
