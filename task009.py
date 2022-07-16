#Проверка строки
#Строка считается действительной, если все символы в строке встречаются
# одинаковое количество раз. Также допустимо, если для выполнения этого
# условия будет достаточно удалить 1 символ из строки. Напишите функцию, 
# которая возвращает True, если строка действительна и False, если нет.
#abc    ->  True  
#abcc   ->  True
#Формат ввода
#abccc
#Формат вывода
#False

#Статистический словарь
def stat_dic(inpstr) :
    st_dic = {}
    for ch in inpstr :
        if not (ch in st_dic) :
            st_dic[ch] = 0
        st_dic[ch] += 1
    return st_dic

#действительный словарь
def valid_dic(st_dic0) :
    stat_compare = {}
    comp_keys = list(st_dic0.keys())
    true_count = 0
    for st in st_dic0.items() :
        if st[1] == st_dic0[comp_keys[0]] :
            stat_compare[True] = st[1]
            true_count += 1
        else :
            stat_compare[False] = st[1]
    if true_count != len(st_dic0) :
        result = (true_count == len(st_dic0)-1) and (stat_compare[True] == stat_compare[False]-1)
    else :
        result = True
    return result
               
#
def valid_sentence(inp_str0):
    return valid_dic(stat_dic(inp_str0))

#
if __name__ == '__main__':
    inp_str = input("введите строку ")
#    print(stat_dic(inp_str))
    print(valid_sentence(inp_str))
