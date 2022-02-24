"""
Финальный проект второго спринта

Модуль фитнес-трекера, который обрабатывает данные для трех видов тренировок:
для бега, спортивной ходьбы и плавания.
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке.

    Принимает параметры:
    training_type — имя класса тренировки;
    duration - длительность тренировки в часах;
    distance — дистанция в километрах, преодолённую за тренировку;
    speed — средняя скорость, пользователя;
    calories — расход килокалорий пользователя тренировку.
    """

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        """Получить сообщение о прошедшей тренировке."""

        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


@dataclass
class Training:
    """Базовый класс тренировки."""
    # Расстояние, которое преодолел спортсмен.
    LEN_STEP: ClassVar[float] = 0.65
    # Константа для перевода значений из метров в километры.
    M_IN_KM: ClassVar[int] = 1000

    # Константа для перевода значений из часа в минуты.
    M_IN_HOUR: ClassVar[int] = 60

    """
    Принимает информацию с датчиков:
    action - количество совершённых действий (число шагов, гребков и пр.);
    duration - длительность тренировки в часах;
    weight - вес спортсмена.
    """

    action: int
    duration: float
    weight: float

    def get_duration_in_minutes(self) -> float:
        """Конвертация длительности тренировки в минуты."""

        return self.duration * self.M_IN_HOUR

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Определите get_spent_calories в '
                                  f'{type(self).__name__}.')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = type(self).__name__

        return InfoMessage(training_type, self.duration, self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories())


@dataclass
class Running(Training):
    """Тренировка: бег."""
    COEFF_CALORIE_1: ClassVar[float] = 18
    COEFF_CALORIE_2: ClassVar[float] = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий по бегу."""

        return ((self.COEFF_CALORIE_1 * self.get_mean_speed()
                 - self.COEFF_CALORIE_2) * self.weight / self.M_IN_KM
                * self.get_duration_in_minutes())


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEFF_CALORIE_1: ClassVar[float] = 0.035
    COEFF_CALORIE_2: ClassVar[float] = 0.029

    # Принимаем доп. параметр height — рост спортсмена.
    height: float

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий по ходьбе."""

        return ((self.COEFF_CALORIE_1 * self.weight
                 + (self.get_mean_speed()**2 // self.height)
                 * self.COEFF_CALORIE_2 * self.weight)
                * self.get_duration_in_minutes())


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: ClassVar[float] = 1.38
    COEFF_CALORIE_1: ClassVar[float] = 1.1
    COEFF_CALORIE_2: ClassVar[float] = 2

    """
    Принимаем доп. параметры:
    length_pool — длина бассейна в метрах;
    count_pool — сколько раз пользователь переплыл бассейн.
    """
    length_pool: float
    count_pool: int

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        return ((self.get_mean_speed() + self.COEFF_CALORIE_1)
                * self.COEFF_CALORIE_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    workout_types = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking,
    }
    if workout_type not in workout_types:
        raise ValueError(f'Тренировка с типом "{workout_type}" '
                         'не поддерживается!')
    return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
