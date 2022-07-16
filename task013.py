#Счётчик строк
#В прикреплённом файле содержится программа, которая вычисляет 
#количество строк кода в некотором каталоге. Не переименовывая 
#функции, допишите недостающий код в функциональном стиле. Императивные 
#конструкции if/for/while в этой задаче использовать нельзя. Допустимо 
#частичное решение.

import codecs

#
def count_line(file_name) :
#    f=open(file_name)
#    count = 0
#    for x in f :
#        if x.strip()[:1]!='#' and x.strip()!='' :
#            count += 1
#    f.close()
#    return count 
    return len(list(filter(lambda x : x.strip()[:1]!='#' and x.strip()!='' ,open(file_name,"r",encoding='utf-8'))))

#
if __name__ == '__main__' :
   inp_str = input('введите имя файла для подсчета строк  ')
   print(count_line(inp_str))
   

