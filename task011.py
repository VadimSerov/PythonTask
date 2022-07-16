#Веб-сайт требует, чтобы пользователи вводили пароль для регистрации,
# соответствующий определенным требованиям. Напишите программу для 
# проверки правильности ввода пароля пользователями.
#Ниже приведены критерии проверки пароля:
#1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
#2. Минимум 1 число от [0–9]
#3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
#4. Минимум 1 специальный символ
#5. Минимальная длина пароля : 6
#6. Максимальная длина пароля: 12
#Программа должна возвращать True или False.
#Формат ввода
#Passw1#0rd
#Формат вывода
#True

#
def check_pass(inpstr) :
    check_dic = {"az_low":"abcdefghijklmnopqrstuwxyz",
                 "az_upp":"ABCDEFGHIJKLMNOPQRSTUWXYZ",
                 "numb":"0123456789",
                 "spec":"!#$%&()*+,-./:;<=>?@[\]^_{|}~"}
    stat_dic = {}
    for key in check_dic.keys() :
        stat_dic[key] = 0
    inpu = inpstr.strip()
    out = True
    if 6<len(inpu) and len(inpu)<12 :
        for ch in inpu :
            not_in = False
            for key in check_dic.keys() :
                not_in = not_in or (ch in check_dic[key])
            out = out and not_in
            for key,content in check_dic.items() :
                if ch in content :
                    stat_dic[key] += 1
        for key in stat_dic.keys() :
            out = out and stat_dic[key]>0   
    else :
        out = False
    return out

#
if __name__ == '__main__' :
   inp_str = input('введите пароль ')
   print(check_pass(inp_str))
