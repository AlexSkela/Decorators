import datetime

def log_decorator(old_function):

    def new_function(*args, **kwargs):

        result = old_function(*args, **kwargs)

        date = datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
        name = str(old_function)

        with open('logs.txt', 'a', encoding='utf-8') as document:
            document.write(date)
            document.write(name)
            document.write(f'Аргументы {args} и {kwargs}')
            document.write(f'Возвращаемое значение - {result} \n')
        return result


    return new_function

@log_decorator
def calc(number1, number2):
    resault = number1 + number2
    return resault


print(calc(2, 3))
print(calc(3, 8))
print(calc(7, 10))