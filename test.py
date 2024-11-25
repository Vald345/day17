def readfile():
    try:
        file_name = input('Введите имя файла и расширение(пример: test.txt) ')
        with open(file_name,'r') as file:
            print("Содержимое файла")
            print(file.read())
    except FileNotFoundError:
        print("Данный файл не найден")
        print(f'Файл {file_name} отсуствует')   
    except PermissionError:
        print("Недостаточно прав для открытия файла")
    except Exception as e:
        print("Что-то пошло не так")
        print(e)

def conver_int():
    while True:
        try:
            numbers = int(input("Введите число: "))
            print(numbers)
            break
        except ValueError:
            print("Не верный ввод")
if __name__ == '__main__':
    readfile()
    conver_int()