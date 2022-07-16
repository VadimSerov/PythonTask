#В данной задаче необходимо определить долю выживших людей 
#("Survived" == 1) в наборе данных, которые удовлетворяют 
#заданному составному фильтру:
#Их возраст ("Age") строго больше заданного числа N
#Их Pclass строго равен заданному числу P
#Количество родственников ("Parch") строго равно заданному числу K
#Формат ввода
#60 1 0
#Формат вывода
#0.2727
#Примечания
#Целые числе выводим без нулей после запятой. Дробные числа выводим
# с точностью до 4 знаков после запятой.
#В случае если никто в наборе данных не удовлетворяет предоставленным 
#фильтрам, выводим долю выживших равной 0
#Обратите внимание, что ожидается НЕ процент, 
#а именно ДОЛЯ выживших людей.

#import codecs
import csv

#
class R_csv :
    def read_scv(self, file_name) :
        csv_file = open(file_name, 'r', newline='', encoding='utf-8')    
        result = list(csv.reader(csv_file, delimiter=',', quotechar='"'))
        csv_file.close()
        return result

#
def r_round(x, n_eps) :
    if (10*x)%10 == 0 :
        res = int(x)
    else :
        res = round(x, n_eps)
    return res

#
def stat_csv_parent(csv_list, age, pclass, parch ) :
    head_list = csv_list[0]
    index_Survived = head_list.index("Survived")
    index_Age = head_list.index("Age")
    index_Pclass = head_list.index("Pclass")
    index_Parch = head_list.index("Parch")
    
    result = {1:0,0:0}
    for row_list in csv_list[1:] :        
        try :
            if float(row_list[index_Age]) > age and int(row_list[index_Pclass]) == pclass  and int(row_list[index_Parch]) == parch :
                result[int(row_list[index_Survived])] += 1
        except :
            continue
 
    if result[0]+result[1] == 0 :
        return 0
    else :
        return result[1]/(result[0]+result[1])
        
#
if __name__ == '__main__':
   inp_list = input(":").strip().split()
   pd = R_csv()  
   print(r_round(stat_csv_parent(pd.read_scv("titanic.csv"), float(inp_list[0]), int(inp_list[1]), int(inp_list[2])),4))
