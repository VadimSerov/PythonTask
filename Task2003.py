# необходимо определить количество людей в наборе данных 
#возраст которых строго больше N. Где N - некое целое число
# от 0 до 100, которое подается на вход вашей функции. 
# На выходе ожидается также целое число - количество 
# пассажиров Титаника.
#Формат ввода 60
#Формат вывода 22

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
def stat_age(csv_list, age) :
    n_age = 0
    age_index = csv_list[0].index("Age")
    for line in csv_list[1:] :
        try :
            if float(line[age_index]) > age :
                n_age += 1 
        except :
            continue	
    return n_age

#
if __name__ == '__main__':
    pd = R_csv()
    print(stat_age(pd.read_scv("titanic.csv"), int(input(":"))))
