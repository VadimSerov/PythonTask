#Анаграммы
#Дана строка текста (кириллица) со словами через пробел. Среди слов найти все пары анаграмм. Пары анаграмм вывести в алфавитном порядке, среди пар сортировка тоже по алфавиту. Каждая пара выводится в новой строке в нижнем регистре.
#Формат ввода
#Кот нос ток сон клад рама вход книга вдох
#Формат вывода
#вдох вход
#кот ток
#нос сон

#ввод понижение разбиение сортировка
str_list  = sorted(input("введите строку с анаграммами ").lower().split(' '))

#поиск анаграмм
anagr_list = []
check = []
for word in str_list :
    word_list = list(word)
    num0 = 0
    while num0<len(word_list) :   
        ch0 = word_list[num0]
        num1 = num0
        while num1<len(word_list) :
            ch1 = word_list[num1]
            word_change_list = word_list.copy()
            word_change_list[num0],word_change_list[num1] = word_list[num1],word_list[num0]
            word_change = "".join(word_change_list)
            if (word_change in str_list) and (word != word_change) and not (word_change in check):
                check.append(word)
                anagr_list.append([word, word_change])
            num1 += 1
        num0 += 1
#вывод 
for anagr in anagr_list :
    print(anagr[0],anagr[1])