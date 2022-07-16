#Самая длинная подстрока
#Напишите функцию, которая возвращает самую длинную
# неповторяющуюся подстроку для входной строки. 
# Если несколько подстрок совпадают по длине, 
# функция возвращает ту, которая встречаетсяqwerrty первой.
#xxxxx     ->   x  
#abcdefa   ->   abcdef
#kjhffkjhabcdefghijhgfdfdsh -> kjhabcdefg
#Формат ввода
#abcabcbb
#Формат вывода
#abc

#
def get_longest_substring(inp):
    current = []
    all_substrings = []
    for c in inp:
        if c in current :
            all_substrings.append(''.join(current))
            cut_off = current.index(c) + 1
            current = current[cut_off:]
        current += c
        all_substrings.append(''.join(current)) 
    return max(all_substrings, key=len)

#
if __name__ == '__main__' :
    print(get_longest_substring(input(" : ")))
