
new_list = input(":").split()
for num in new_list :
    try :
        max0 = max(max0,float(num))
    except :
        max0 = float(num)
print(max0)
