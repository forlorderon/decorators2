import time
from functools import lru_cache
import logging

# ------------------------------------

# Простой пример декоратора

def my_decorator(func):
    def wrapper():
        print("Начало загрузки...")
        func()
        print("Загрузка завершена!")
    return wrapper

@my_decorator
def loading():
    print("..................")
loading()

# ------------------------------------

# Декоратор с параметрами

# def parametr_decorator(arg):
#     def actual_decorator(func):
#         def wrapper():
#             print(f"Декоратор с аргументом: {arg}")
#             func()
#         return wrapper
#     return actual_decorator

# @parametr_decorator("Параметр")
# def my_function():
#     my_function()

# ------------------------------------


#Комбинирование декораторов

# @decorator1
# @decorator2
# def my_function():

# ------------------------------------

# Декоратор для измерения времени выполнения функций

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
#         return result
#     return wrapper

# @timing_decorator
# def example_function():
#     time.sleep(2)

# example_function()

# ------------------------------------

# Декораторы для кэширования результатов

# @lru_cache(maxsize=None)
# def cached_function(arg):
#     result = arg * 2
#     print(f"Выполнение вычеслений для аргумента{arg}")
#     return result

# result1 = cached_function(5)
# result2 = cached_function(5)
# result3 = cached_function(10)

# ------------------------------------

# Декораторы для логирования 

# def log_function(func):
#     def wrapper(*args, **kwargs):
#         logging.info(f"Вызов функции {func.__name__} с аргументами {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"Функция {func.__name__} вернула результат: {result}")
#         return result
#     return wrapper

# logging.basicConfig(level=logging.INFO)

# @log_function
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(3, 5)

# ------------------------------------

# Декораторы для обработки исключений

# def handle_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(f"Возникло исключение в функции {func.__name__}: {e}")
#             return None
#     return wrapper

# @handle_exceptions
# def divide(a, b):
#     return a / b

# result = divide(5, 0)


