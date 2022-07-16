#В данном наборе, в столбце "Age" есть пропуски, то есть 
#некоторые значения ячеек не цифры, а None. Для заполнения 
#None в pandas есть специальный инструмент 
#df["Название столбца"].fillna("заполнитель"). Где заполнителем может быть
# число, или строка, или другой объект, в зависимости от типа столбца.
# В столбце "Age" хранятся числовые объекты - float.
#Ваша задача принять из stdin значение (тип float) и заполнить 
#им пропуски в столбце "Age" и вернуть среднее значение столбца "Age".
#Формат ввода
#0.0
#Формат вывода
#23.7993
#Примечания
#Округление производить до 4-х знаков после запятой

#import codecs
import csv

#
class R_csv :
    def read_scv(self,file_name) :
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
def aver_Age(csv_list, repl_float) :
    head_list = csv_list[0]
    index_Age = head_list.index("Age")
    sum_float = 0.0
    for row_list in csv_list[1:] :
        try :
            sum_float += float(row_list[index_Age])
        except:
            sum_float += repl_float
    return sum_float/len(csv_list[1:])

if __name__ == '__main__':
    repl_float = float(input(":").strip())
    pd = R_csv()
    print(r_round(aver_Age(pd.read_scv("titanic.csv"), repl_float), 4))
