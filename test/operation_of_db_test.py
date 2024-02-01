import sqlite3

def select_area(unit_number):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT person.* '
                   f'FROM apartment '
                   f'INNER JOIN person '
                   f'ON apartment.number_of_apartment = person.number_of_apartment '
                   f'WHERE '
                   # f'person.number_of_apartment == {number_of_apartment} AND '
                   f'apartment.unit == {unit_number}')
    cur = cursor.fetchall()
    connection.close()
    return cur


def select_person_area(person_id):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT area '
                   f'FROM person '
                   f'WHERE '
                   f'id == {person_id}')
    cur = cursor.fetchone()
    connection.close()
    return cur


def select_apartment_count(unit_number):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT COUNT(*), SUM(area) '
                   f'FROM apartment '
                   f'WHERE apartment.unit == {unit_number}')
    cur = cursor.fetchone()
    connection.close()
    return cur


def select_person_count(unit_number):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT COUNT(*) '
                   f'FROM person '
                   f'INNER JOIN apartment '
                   f'ON person.number_of_apartment = apartment.number_of_apartment '
                   f'WHERE apartment.unit == {unit_number}')
    cur = cursor.fetchone()
    connection.close()
    return cur


area_of_house = round(select_apartment_count(1)[1], 2)
count = int(select_apartment_count(1)[0])
area = 0

for i in select_area(1):
    print(i)
    area += i[-3]


def select_vote_yes_on_meeting(person_id):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * '
                   f'FROM person '
                   f'INNER JOIN vote_for_questions '
                   f'ON vote_for_questions.id_person = person.id '
                   f'WHERE person.id = {person_id} AND vote_for_questions.vote = 1 ')
    cur = cursor.fetchone()
    connection.close()
    return cur


def select_vote_no_on_meeting(person_id):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * '
                   f'FROM person '
                   f'INNER JOIN vote_for_questions '
                   f'ON vote_for_questions.id_person = person.id '
                   f'WHERE person.id = {person_id} AND vote_for_questions.vote = 0 ')
    cur = cursor.fetchone()
    connection.close()
    return cur


def select_vote_yes_in_writing(person_id):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * '
                   f'FROM person '
                   f'INNER JOIN vote_for_questions '
                   f'ON vote_for_questions.id_person = person.id '
                   f'WHERE person.id = {person_id} AND vote_for_questions.vote = 11 ')
    cur = cursor.fetchone()
    connection.close()
    return cur


def select_vote_no_in_writing(person_id):
    connection = sqlite3.connect('../data/database.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * '
                   f'FROM person '
                   f'INNER JOIN vote_for_questions '
                   f'ON vote_for_questions.id_person = person.id '
                   f'WHERE person.id = {person_id} AND vote_for_questions.vote = 10 ')
    cur = cursor.fetchone()
    connection.close()
    return cur


i = 1

area_yes, area_no, area_yes_w, area_no_w = 0, 0, 0, 0
count_yes, count_no, count_yes_w, count_no_w = 0, 0, 0, 0

while i < select_person_count(1)[0]:
    if select_vote_yes_on_meeting(i):
        # print(f'+ {select_vote_yes_on_meeting(i)[0:4]}')
        area_yes += select_person_area(i)[0]
        count_yes += 1
    elif select_vote_no_on_meeting(i):
        # print(f'- {select_vote_no_on_meeting(i)[0:4]}')
        area_no += select_person_area(i)[0]
        count_no += 1
    elif select_vote_yes_in_writing(i):
        # print(f'++ {select_vote_yes_in_writing(i)[0:4]}')
        area_yes_w += select_person_area(i)[0]
        count_yes_w += 1
    elif select_vote_no_in_writing(i):
        # print(f'-- {select_vote_no_in_writing(i)[0:4]}')
        area_no_w += select_person_area(i)[0]
        count_no_w += 1
    i += 1

print(' ')
print(f'Кількість квартир: {count}')
print(f'Площа будинку: {area_of_house}')
print(f'Площа заселена: {round(area, 2)}')
print(f'Кількість жителів: {(select_person_count(1)[0])}')
print('------------------------------AREA----------------------------------')
print(f'Yes {round(area_yes, 2)} m2')
print(f'NO {round(area_no, 2)} m2')
print(f'YesW {round(area_yes_w, 2)} m2')
print(f'NOW {round(area_no_w, 2)} m2')
print('------------------------------COUNT----------------------------------')
print(f'Yes {count_yes}')
print(f'NO {count_no}')
print(f'YesW {count_yes_w}')
print(f'NOW {count_no_w}')
#
#
# num_app = 1
# count = 1
# area = 0
#
# appart = operation_for_db.SQLiteDBPerson(count, num_app, 2, 1, '../data/database.db')
# app_count = appart.select_appartment_count()
# app_count = int(app_count.fetchone()[0])
# print(f'Загальна кіслькість квартир: {app_count}')
# # print(appart.select_vote_yes().fetchall())
#
# while num_app < app_count:
#     count = 1
#     appart = operation_for_db.SQLiteDBPerson(count, num_app, 2, 1, '../data/database.db')
#         print(appart.select_area().fetchone())
#     # for i in appart.fetchall():
#     #     print(f"{count} + {appart.select_vote_no().fetchone()}")
#     #     # print(i[-1])
#     #     # if appart.select_vote_yes().fetchall():
#     #     #     area += i[-1]
#     #     #     print(area)
#     count += 1
#     num_app += 1
#
# print(f'Yes - {area}')
#
#
# while num_app < app_count:
#     appart = operation_for_db.SQLiteDBPerson(count, num_app, 2, 1, '../data/database.db')
#     appart.select_area()
#     # for i in appart.fetchall():
#         # print(appart.select_vote_no().fetchone())
#         # print(i[-1])
#         # if appart.select_vote_yes().fetchall():
#         #     area += i[-1]
#         #     print(area)
#         # count += 1
#     num_app += 1
#
# print(f'No - {area}')
