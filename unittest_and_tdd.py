"""
1.
Напишите тесты на метод divider() класса Calculator. Сам метод пока не написан, но есть docstring с его описанием.
Проверьте:
правильно ли работает деление;
выбрасывается ли исключение при делении на 0.
Подсказка

2.
Напишите метод divider. Решение будет засчитано, если метод пройдёт ваши тесты.
Подсказка

3.
В коде задания описан метод summ.
Если вызвать этот метод без аргументов, он вернёт ноль, а если передать в метод summ один аргумент — он вернёт значение этого аргумента.
Это не лучшее поведение для калькулятора, надо его изменить. Методика TDD подразумевает, что сначала пишутся тесты, а потом код.
В этом задании напишите тесты, которые проверяют, что summ возвращает None, если количество переданных аргументов меньше двух.
Подсказка

4.
Доработайте метод summ: он должен возвращать None, если вызывается с одним аргументом или без аргументов.
"""


import unittest


class Calculator:
    """Производит различные арифметические действия."""
    @staticmethod
    def summ(*args):
        """Возвращает сумму принятых аргументов."""
        if len(args) < 2:
            return None
        return sum(i for i in args)

    @staticmethod
    def divider(self, num1, num2):
        """Возвращает результат деления двух чисел."""
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Нельзя делить на ноль")
            raise ZeroDivisionError


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_divider(self):
        act = TestCalc.calc.divider(4, 2)
        self.assertEqual(act, 2, 'Неправильный результат деления!'
                                 'С таким расчетом космоса нам не видать :(')

    def test_divider_zero_division(self):
        # Проверьте, что деление на 0 выбрасывает исключение
        with self.assertRaises(ZeroDivisionError):
            TestCalc.calc.divider(4, 0)

    def test_summ(self):
        act = TestCalc.calc.summ(3, -3, 5)
        self.assertEqual(act, 5, 'summ работает неправильно')

    def test_summ_no_argument(self):
        act = TestCalc.calc.summ()
        self.assertIsNone(act)

    def test_summ_one_argument(self):
        act = TestCalc.calc.summ(1)
        self.assertIsNone(act)
