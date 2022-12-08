# task 1

import sys
from datetime import datetime


original_write = sys.stdout.write


def my_write(string_text):
    current_date_and_time = datetime.now()
    current_date_and_time_string = \
        current_date_and_time.strftime("[%d-%m-%Y %H:%M:%S]: ") + string_text
    if len(string_text.rstrip()) != 0:
        original_write(current_date_and_time_string)
    else:
        original_write(string_text)


sys.stdout.write = my_write

print('1, 2, 3')

sys.stdout.write = original_write

# task 2


def timed_output(function):
    def wrapper(*args, **kwargs):
        original_write = sys.stdout.write
        sys.stdout.write = my_write
        function(*args, **kwargs)
        sys.stdout.write = original_write
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


print_greeting("Nikita")

# task 3


def redirect_output(filepath):
    def decorator(func):
        def wrapper():
            original_stdout = sys.stdout
            with open(filepath, 'w') as output:
                sys.stdout = output
                func()
                sys.stdout = original_stdout
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


calculate()
