from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats

# Завдання 1: Перевірка свят та робочих днів
print("\n--- Ukrainian Calendar ---")
calendar = UkrainianCalendar()
print("Свята:", calendar.get_holiday_list())  # Вивід списку свят
print("2025-01-01 робочий день?", calendar.is_working_day("2025-01-01"))  # Новорічний день
print("2025-01-02 робочий день?", calendar.is_working_day("2025-01-02"))  # Звичайний день

# Завдання 2: Проста калькуляторна програма
print("\n--- Calculator ---")
calc = Calculator()
a = float(input("Введіть перше число: "))  # Введення першого числа
b = float(input("Введіть друге число: "))  # Введення другого числа
operation = input("Оберіть операцію (+, -, *, /): ")  # Вибір операції
if operation == "+":
    print("Результат:", calc.add(a, b))
elif operation == "-":
    print("Результат:", calc.subtract(a, b))
elif operation == "*":
    print("Результат:", calc.multiply(a, b))
elif operation == "/":
    print("Результат:", calc.divide(a, b))
else:
    print("Невідома операція")

# Завдання 3: Аналіз тексту
print("\n--- Text Analysis ---")
text = input("Введіть текст: ")  # Введення тексту користувачем
stats = TextStats(text)
print("Кількість слів:", stats.count_words())  # Підрахунок слів
print("Найпоширеніша літера:", stats.most_common_letter())  # Пошук популярної літери
