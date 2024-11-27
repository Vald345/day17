def big_masiv(massiv,index):
    try:
        index = int(index)
        return massiv[index]
    except IndexError:
        return "Данных в этой ячейке нету"
    except ValueError:
        return "Введено не число"
mas = [1,2,3,4,5,6,7,8]
ind = input("Введите число: ")
print(big_masiv(mas,ind))