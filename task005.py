#Формат ввода
#кот арбуз слово завтрак кнопка лес Лоб
#45
#Формат вывода
#кот кнопка Лоб

#
def make_t9_temp(t9_list,t9_dict,inp_str) :
    #сборка временого списка
    t9_temp = t9_list.copy()
    t9_temp0 = []
    count = 0
    for digit in inp_str :
        for word in t9_temp :
            word0 = word.lower().strip()
            if count<len(word0) and (word0[count] in t9_dict[digit]) and not (word0 in t9_temp0) :
                t9_temp0.append(word)
        count += 1
        t9_temp = t9_temp0.copy()
        t9_temp0 = []
    return t9_temp
#

#заполнение словаря t9
#t9_list1 = ["кот","арбуз","слово","завтрак","кнопка","лес","Лоб"]
t9_dict1 = {"1":".,-","2":"абвг","3":"дежз","4":"ийкл","5":"мноп","6":"рсту",
                "7":"фхцч","8":"шщъы","9":"ьэюя"}
 
t9_list1 = input("введите словарик T9 ").split()
inp_str = input("введите число для T9 ").strip()

for word in make_t9_temp(t9_list1,t9_dict1,inp_str) :
    print(word)

