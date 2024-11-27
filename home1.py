def plus_two(numb):
    try:
        numb = int(numb)
        return numb + 2
    except ValueError:
        return "Ожидаемый тип данных — число!"
numver = input("Введите число: ")
print(plus_two(numver))