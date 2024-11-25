def check_num(number,number1):
    try:
        return(int(number)+int(number1))
    except ValueError:
        return(str(number)+str(number1))

def check_big_num(number):
    try:
        number = str(number)
        summ = 0
        step = 0
        delit = 1
        while step < len(number):
            summ += int(number[step])
            delit = delit * int(number[step])
            step+=1
        return summ, delit
    except ValueError:
        return "Не верный ввод"
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    

#str1 = input("Введите первую строку: ")
#str2 = input("Введите вторую строку: ")
#print(check_num(str1,str2))
str3 = input("Введите число: ")
print(check_big_num(str3))