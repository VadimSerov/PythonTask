#Цвет
#На вход в программу поступает цвет CSS RGB(A), необходимо определить
# действителен ли его формат. Создайте функцию, которая принимает
# строку (например, «rgb (0, 0, 0)») и возвращает True, если формат
# правильный, в противном случае возвращает False. Данные могут поступать
# как в формате rgb, так и rgba.
#Допустимые значения: rgb(0-255, 0-255, 0-255),
#					 rgb(0-100%, 0-100%, 0-100%),
#					 rgba(0-255, 0-255, 0-255, 0-1)  
#Возможные форматы ввода:  
#rgb(0%,50%,100%) ---> True  
#rgba(0,0,0,0)    ---> True  
#rgb(255,255,255) ---> True  
#rgb(0,,0)        ---> False  
#rgb(-1,0,0)      ---> False  
#rgba(0,0,0,1.5)  ---> False  
#rgba(0,0,0,0.5)  ---> True
#Формат ввода
#rgb(-1,0,0)
#Формат вывода
#False

#
def check_rgb(inpstr) : 
    out = True
    if "rgba" in inpstr :
        arg_str = inpstr.replace("rgba","").replace("(","").replace(")","").strip()
        arg_list = arg_str.split(',')
        out = out and len(arg_list) == 4
        i= 1
        for arg0 in arg_list :
            if i<4 :
                try :
                    n_arg = int(arg0)
                    out = out and (-1<n_arg and n_arg<256)
                except :
                    out = False
            else :
                try :
                    n_arg = float(arg0)
                    out = out and (0<=n_arg and n_arg<=1)
                except :
                    out = False
            i += 1
    elif "rgb" in inpstr :
        arg_str = inpstr.replace("rgb","").replace("(","").replace(")","").strip()
        arg_list = arg_str.split(',')
        out = out and len(arg_list) == 3
        if "%" in arg_str :
            check_procent = True
            for argu in arg_list :
                check_procent = check_procent and ("%" in argu)
            if check_procent :
                for arg0 in arg_list :
                    arg = arg0.replace("%","")
                    try :
                        n_arg = int(arg)
                        out = out and (-1<n_arg and n_arg<101)
                    except :
                        out = False
            else :
                out = False
        else:
            for arg0 in arg_list :
                try :
                    n_arg = int(arg0)
                    out = out and (-1<n_arg and n_arg<256)
                except :
                    out = False             
    else :
        out = False
    return out
#
if __name__ == '__main__' :
   inp_str = input('введите строку - фукцию цвета ')
   print(check_rgb(inp_str))

