# Финальный проект первого спринта

import datetime as dt

FORMAT = '%H:%M:%S' # Формат времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if None in data or len(data) != 2:
        return False
    return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data and time <= max(storage_data):
        return True
    return False


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return sum(storage_data.values()) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return round(steps * STEP_M / 1000, 2)


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    hours = round(current_time.hour+current_time.minute/60.0, 2)
    minutes = hours * 60
    mean_speed = dist / hours

    spent_calories = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * minutes
    return round(spent_calories, 2)


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


def show_message(*args):
    pack_time, day_steps, dist, spent_calories, achievement = args
    print(f"""
Время: {pack_time}.
Количество шагов за сегодня: {day_steps}.
Дистанция составила {dist} км.
Вы сожгли {spent_calories} ккал.
{achievement}
""")

def accept_package(data):
    """Обработать пакет данных."""
    if not check_correct_data(data):
        return 'Некорректный пакет'
    
    time_str, steps = data
    # Строка с временем в объект time.
    pack_time = dt.datetime.strptime(time_str, '%H:%M:%S').time()

    if check_correct_time(pack_time):
        return 'Некорректное значение времени'

    # Подсчёт пройденных шагов.
    day_steps = get_step_day(steps)
    # Расчёт пройденной дистанции.
    dist = get_distance(day_steps)
    # Расчёта сожжённых калорий.
    spent_calories = get_spent_calories(dist, pack_time)
    # Мотивирующее сообщение.
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    # Новый элемент в словарь storage_data.
    storage_data[pack_time] = day_steps
    return storage_data


# Данные для самопроверки.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
