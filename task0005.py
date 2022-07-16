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
            word0 = word.lower()
            if count<len(word0) and (word0[count] in t9_dict[digit]) and not (word0 in t9_temp0) :
                t9_temp0.append(word)
        count += 1
        t9_temp = t9_temp0.copy()
        t9_temp0 = []
    return t9_temp

#
def select_t9_list(t9_temp, com ) :
    if len(com) < len(t9_temp) :
        return t9_temp[len(com)]
    else :
        return t9_temp[len(t9_temp)-1]

#заполнение словаря t9
t9_list1 = ["кот","арбуз","слово","завтрак","кнопка","лес","Лоб"]
t9_dict1 = {"1":".,-","2":"абвг","3":"дежз","4":"ийкл","5":"мноп","6":"рсту",
                "7":"фхцч","8":"шщъы","9":"ьэюя"}
                
inp_str = input("введите число для t9 или число и несколько символов V : ").strip()


if inp_str.isdigit() :

    t9_temp1 = make_t9_temp(t9_list1,t9_dict1,inp_str)

# вывод временного списка
    for word in t9_temp1 :
        print(word,end=' ')
    print()
    
    key_str = input("теперь введите несколько символов V(-'стрелка вниз') чтобы выбрать слово из списка. пустой ввод выберет первое слово ").strip()
    if bool(t9_temp1) :
        print(select_t9_list(t9_temp1,key_str))
    else :
        print("не подобран список t9 ")
else :
    valid = True
    i = 1
    for k in inp_str :
        valid = valid and ( k in t9_dict1.keys() or k == "V" )
        if k in t9_dict1.keys() :
            i_digit = i
        i += 1
    if valid :
        t9_temp2 = make_t9_temp(t9_list1,t9_dict1,inp_str[:i_digit])
        if bool(t9_temp2) :
            print(t9_temp2)
            print(select_t9_list(t9_temp2,inp_str[i_digit:]))
        else :
            print("не подобран список t9 ")
    else :
        print("не верный ввод для T9")
