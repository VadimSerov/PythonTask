#Статистика символов
#Формат ввода
#Hello 123 ** hello мама
#Формат вывода
#e 2
#h 2
#l 4
#o 2
#а 2
#м 2

# ввод
str0=input("введите строку для статистики ").lower()
#сортировка
#unique=sorted(set(list(str0)))
unique = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя')

#формирование списка и вывод
out0 = []
for symbol in unique :
    count0 = str0.count(symbol)
    if 0 != count0 :
        out0.append({symbol:count0})
        print(symbol,count0)
#print(out0)
