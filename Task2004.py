#Каждая строка набора данных - это отдельный человек, 
#который либо выжил, либо не выжил (столбец "Survived").
#В данной задаче необходимо определить один из
# статистических показателей: количество, максимум, 
#минимум - по указанной группе пассажиров, по указанному 
#признаку. Например, найти количество представителей 
#выживших/не выживших пассажиров ("Survived") по столбцу "Pclass".
#На вход получаем: столбец по которому группируем, столбец для 
#которого ищем статистику, название самой статистики (count, min, max)
#На выходе печатаем столько строк, сколько получилось после 
#группировки по указанному столбцу. В каждой строке сначала
# название группы (уникальное значение столбца, по которому группировали), 
#затем пробел, затем значение статистики для указанной группы.
#Формат ввода
#Survived Pclass count
#Формат вывода
#0 549
#1 342

import csv

#
class R_csv :
    def read_scv(self,file_name) :
        csv_file = open(file_name, 'r', newline='', encoding='utf-8')    
        result = list(csv.reader(csv_file, delimiter=',', quotechar='"'))
        csv_file.close()
        return result
    
#
def csv_stat(lines_csv, group, stat, command) :
    head_list = lines_csv[0]
    group_index = head_list.index(group)
    stat_index = head_list.index(stat)
    result_dict = {}    
    for row_list in lines_csv[1:] :        
        if command == "max" :
            try :
                result_dict[row_list[group_index]] = max(result_dict[row_list[group_index]],row_list[stat_index])
            except :
                result_dict[row_list[group_index]] = row_list[stat_index]
        elif command == "min" :
            try :
                result_dict[row_list[group_index]] = min(result_dict[row_list[group_index]],row_list[stat_index])
            except :
                result_dict[row_list[group_index]] = row_list[stat_index]
        elif command == "count" :
            try :
                result_dict[row_list[group_index]] += 1
            except :
                result_dict[row_list[group_index]] = 1        
    return result_dict
    
#
if __name__ == '__main__':
    inpu = input(':').split()
    pd = R_csv()
    csv_dict = csv_stat(pd.read_scv("titanic.csv"), inpu[0], inpu[1], inpu[2])
    for key, value in  csv_dict.items() :
        print(key, value)
