import random

last_name = (
    'Попова', 'Васильев', 'Горбачева', 'Громова', 'Устинова', 'Рыбаков', 'Иванов', 'Кочетков', 'Романова', 'Кошелев'
)

first_name = (
    'Алексей', 'Валерия', 'Лука', 'Амина', 'Вероника', 'Даниил', 'Мария', 'Дамир', 'Вероника', 'Михаил'
)

surname = ('Викторович', 'Сергеевич', 'Павлович', 'Петрович', 'Александрович', 'Евгеньевич', 'Русланович',
           'Тимурович', 'Романович', 'Егорович', 'Олегович', 'Дмитриевич', 'Рустамович', 'Валентинович', 'Борисович')

print(f'\nФамилия: {random.choice(last_name)}.\nИмя: {random.choice(first_name)}.\nОтчество: {random.choice(surname)}.')
#
with open('random_fio.txt', 'a', encoding='utf-8') as file:
    file.write(
        f'\nФамилия: {random.choice(last_name)}.\nИмя: {random.choice(first_name)}.\nОтчество: {random.choice(surname)}.\n')
    file.close()
