#Среднее арифметическое
#Создайте функцию, которая принимает переменное количество аргументов
# и находит среднее арифметическое ненулевых из них.
#Обратите внимание на формат вывода
#1 2 3        --->   2  
#2 0 0 2 2    --->   2  
#2 0 2 1 1    --->   1.5
#Формат ввода
#1 2 3 0 0
#Формат вывода
#2


#функция
def average(*nums):
    sum0 = 0
    count = 0
    for x in nums:
        if isinstance(x, list) :
            for x0_str in x :
                try :
                    x0 = float(x0_str)
                except :
                    x0 = 0
                if x0 != 0 :
                    sum0 += x0
                    count += 1
        elif isinstance(x, float) :
            if x !=0 :
                sum0 += x
                count += 1
        elif isinstance(x, int) :
            x = float(x)
            if x !=0 :
                sum0 += x
                count += 1
        aver = 10*sum0/count
        if aver%10 == 0 :
            result = int(aver/10)
        else:
            result = aver/10
    return result

if __name__ == '__main__':
#   print(average(1, 2, 3, 0, 0))
#ввод и разбиение
    inp_list = input("введите числа для подсчёта ").split(' ')
    print(average(2/3,0,1/3))
    print(average(1.4,1/5,0,25,25,25))
    print(average(inp_list))
