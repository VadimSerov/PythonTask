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
    az_low = "abcdefghijklmnopqrstuwxyz"
    az_upp = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    numb = "0123456789"
    spec = "!#$%&()*+,-./:;<=>?@[\]^_{|}~"
    inpu = inpstr.strip()
    out = True
    if 6<len(inpu) and len(inpu)<12 :
        hit1 = 0
        hit2 = 0
        hit3 = 0
        hit4 = 0
        for ch in inpu :
            out = out and ((ch in az_low) or (ch in az_upp) or (ch in numb) or (ch in spec))
            if ch in az_low :
                hit1 += 1
            elif ch in az_upp :
                hit2 += 1
            elif ch in numb :
                hit3 += 1
            elif ch in spec :
                hit4 += 1
        out = out and hit1 > 0 and hit2>0 and hit3>0 and hit4>0
        
    else :
        out = False
    return out

#
if __name__ == '__main__' :
   inp_str = input('введите пароль ')
   print(check_pass(inp_str))
