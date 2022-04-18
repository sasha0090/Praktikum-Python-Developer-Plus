"""
Напишите тесты, которые проверят, что будет, если:
- передать в функцию список чисел int и float вперемешку;
- передать в функцию список, состоящий из чисел и строк;
- передать в функцию пустой список.
"""


def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result


mixed_numbers = [1, 4, 1.3, 5]
result_numbers = '141.35'
assert series_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() не работает со списком чисел')

mixed_numbers_strings = [1, '2', '2', 1]
result_numbers_strings = '1221'
assert series_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() не работает со смешанным списком')

empty = []
result_empty = ''
assert series_sum(empty) == result_empty, (
    'Функция series_sum() не работает с пустым списком')

# ------------------------------------------------

"""
Протестируйте методы programmer_define() и age_define() класса Contact.
Тестировать нужно все состояния: в метод programmer_define() надо по очереди
передать False и True, а в age_define() надо проверить все возрастные категории.
Для проверки всех возможных вариантов создайте несколько экземпляров класса 
Contact с разными значениями полей year_birth и is_programmer.
"""


class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())


test_old_none_programmer = Contact('Пушкин', 1799, False)
assert test_old_none_programmer.programmer_define() == "Нормальный", (
    "Он может и не нормальный, но точно не программист")
assert test_old_none_programmer.age_define() == "Старейшина", (
    "Что-то нет так при его жизни только открыли электричество")


test_old_none_programmer = Contact('Дуров', 1984, True)
assert test_old_none_programmer.programmer_define() == "Программист", (
    "Уже не Российский, но все еще русский программист")
assert test_old_none_programmer.age_define() == "Молодой", (
    "Уже отправляем сообщение в телеграмме, а не в телеграф")


test_old_none_programmer = Contact('Линус', 1969, True)
assert test_old_none_programmer.age_define() == "Олдскул", (
    "Еще не в прошлом, но уже не молод")
