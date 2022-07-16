#Самая длинная подстрока
#Напишите функцию, которая возвращает самую длинную
# неповторяющуюся подстроку для входной строки. 
# Если несколько подстрок совпадают по длине, 
# функция возвращает ту, которая встречаетсяqwerrty первой.
#xxxxx     ->   x  
#abcdefa   ->   abcdef
#Формат ввода
#abcabcbb
#Формат вывода
#abc

#список подстрок
def substr_list(inpstr) :
    sub_list = []
    substr = ""
    for ch in inpstr :
        substr += ch
        head = inpstr[:len(substr)]
        if (substr in inpstr) and not (substr in sub_list) :
            inpstr = head+inpstr.replace(head,'')
            sub_list.append(head)
    #print(sub_list)
    return sub_list
    
#
def max_in_list(sub_list0) :
    max_len = 0
    for word in sub_list0 :
        if max_len<len(word) :
            max_len = len(word)
            sub0 = word
    return sub0
    
#
def max_substr(in_str) :
#    return max(substr_list(inp_str))    
    return max_in_list(substr_list(inp_str))
    
#
if __name__ == '__main__':
    inp_str = input("введите строку с подстроками ")
    print(max_substr(inp_str))
