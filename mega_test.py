class custom_error(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(f'[Ошибка {error_code}]: {message}')

def divide_numbers(a,b):
    if b == 0:
        raise custom_error('Деление на 0 не возможно', 400)
    return a/b

try:
    result = divide_numbers(10,0)
    print(f'Результат {result}')
except custom_error as e:
    print(f'Произошло исключение: {e}')