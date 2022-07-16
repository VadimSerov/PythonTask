#Самая длинная подстрока
#Напишите функцию, которая возвращает самую длинную
# неповторяющуюся подстроку для входной строки. 
# Если несколько подстрок совпадают по длине, 
# функция возвращает ту, которая встречается первой.
#xxxxx     ->   x  
#abcdefa   ->   abcdef
#Формат ввода
#abcabcbb
#Формат вывода
#abc
import csv 

#
def get_longest_substring(input0):
    current = []
    all_substrings = []
    for c in input0:
        if c in current :
            all_substrings.append(''.join(current))
            cut_off = current.index(c) + 1
            current = current[cut_off:]
        current += c
        print(current,2)
        all_substrings.append(''.join(current)) 
    return max(all_substrings, key=len)

#
if __name__ == '__main__' :
#    print(get_longest_substring(input(" : ")))
    csv_file = open("titanic.csv", 'r', newline='', encoding='utf-8')
    
    spamreader = list(csv.reader(csv_file, delimiter=',', quotechar='"'))
    
    print(spamreader)
    csv_file.close()
