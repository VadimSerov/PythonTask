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
    instr = inpstr.strip().upper()+"   "
    sums = 0
    i = 0
    ch0=instr[:3]
    for ch in instr :
        if ch0 != "CCC" and ch == "С" and (instr[i+1:i+2] == "D" or instr[i+1:i+2] == "M") :
            sums -= 100            
        elif ch0 != "XXX" and  ch == "X" and (instr[i+1:i+2] == "L" or instr[i+1:i+2] == "C") :
            sums -= 10
        elif ch0 != "III" and ch == "I" and (instr[i+1:i+2] == "V" or instr[i+1:i+2] == "X") :
            sums -= 1
        else :
            try :
                sums += rom_dict[ch]
            except :
                pass
        ch0 = instr[i:i+3]        
        i += 1
    return sums

#
if __name__ == '__main__' :
   inp_str = input('введите римское число ')
   print(rom_to_arab(inp_str))
