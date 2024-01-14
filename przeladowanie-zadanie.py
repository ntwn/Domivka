class User:
  def __init__(self, name, password, email):
    self.name = name
    self.password = password
    self.email = email
  
  def __str__(self):
    return f'Imię: {self.name} \npassword: {self.password}\nemail: {self.email}\n'

class Program:
  def __init__(self):
    self.users = []
    self.is_working = True
  
  def create_user(self):
    name = input('wprowadź imię usera: ')
    password = input('Wprowadź hasło usera: ')
    email = input('Wprowadź mail usera: ')
    new_user = User(name, password, email)
    self.users.append(new_user)

  def save_users(self):
    with open('user.txt', 'w', encoding='utf-8') as file:
      for i, user in enumerate(self.users, start = 1):
        file.write(f'{i}. {str(user)}')
  
  def print_menu(self):
    while self.is_working:
      print('Dostepne opcje:\n 1. Dodaj użytkownika \n 2. Zapisz użytkowników \n 3. Zamknij program')
      wybor = input('Dokonaj wyboru: ')
      self.execute_command(int(wybor))
  
  def execute_command(self, wybor):
    if wybor == 1:
      self.create_user()
    elif wybor == 2:
      self.save_users()
    else: 
      self.is_working = False


def main():
  users_program = Program()
  users_program.print_menu()

if __name__ == '__main__':
  main()
