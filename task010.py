#Римские цифры
#Создайте функцию, которая принимает на вход римское число
# как строку и преобразует ее в целое число, возвращая результат. 
# Функция должна работать для всех римских цифр, представляющих
# натуральные числа меньше 4000.
#Формат ввода
#MMMCMV
#Формат вывода
#3905

#
def rom_to_arab(inpstr) :
    rom_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    incl_dict = {"CM":900,"CD":400,"XC":90,"XL":40,"IX":9,"IV":4}
    instr0 = inpstr.strip().upper()
    sums = 0
    count = 4000
    prev = 4000
    while instr0!="" :
        ch0=instr0[:2]
        if ch0 in incl_dict.keys() :
            count = incl_dict[ch0]
            if count<=prev :             
                sums += count
                prev = count
            else :
                print("-2-не римское число")
                sums = 0
                break
        else :
            ch0 = instr0[:1]
            if ch0 in rom_dict.keys() :
                count = rom_dict[ch0]
                if count<=prev :
                    sums += count
                    prev = count 
                else :
                    print("-1-не римское число")
                    sums = 0
                    break
            else :
                print("не римское число")
                sums = 0
                break
        instr0 = instr0.replace(ch0,'',1)
    return sums

#
if __name__ == '__main__' :
   inp_str = input('введите римское число ')
   print(rom_to_arab(inp_str))
