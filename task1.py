def check_num(number,number1):
    try:
        number = int(number)
        number1 = int(number1)
        return(number+number1)
    except ValueError:
        return(str(number)+str(number1))
        
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
print(check_num(str1,str2))