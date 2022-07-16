#Самое длинное слово
#Напишите функцию, которая будет возвращать самое длинное слово в предложении. Если найдено более одного слова, то функция возвращает первое.
#Формат ввода
#The Tower of London was built in the 15th century
#Формат вывода
#century

#функция
def max_len_word(inpstr) :
    inp_list = inpstr.split(' ')
    max_len = 0
    for word in inp_list :
        if max_len<len(word) :
            out_word = word
            max_len = len(word)
    return out_word
            
if __name__ == '__main__':
#ввод 
    inp0 = input("введите предложение ")
    print(max_len_word(inp0))
