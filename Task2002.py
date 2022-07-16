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
def forex_csv_2_json(csv_list) :
    st = ""
    key_list = csv_list[0]
    for cont_list in  csv_list[1:] :
        st0 = ""
        body0 = ""
        for key0,cont0 in zip(key_list,cont_list) :
            if key0 == "Valute":
                st0 = 8*' '+'"'+cont0+'":{\n'  
            else :
                if key0 != "Nominal" and key0 != "Value" :
                    cont1 = '"'+cont0+'"'
                else :
                    cont1 = cont0
                if key0==key_list[-1] :
                    body0 += 12*' '+'"'+key0+'":'+cont1+'\n' 
                else :
                    body0 += 12*' '+'"'+key0+'":'+cont1+',\n' 
        if cont_list == csv_list[-1] :
            tail0 = "}\n"
        else :
            tail0 = "},\n"
        st += st0+body0+8*" "+tail0
    return st

#
if __name__ == '__main__':
    csv_filename = input("введите имя файла csv (пустой ввод введет data_bank.csv) ").strip()
    if csv_filename == "" :
        csv_filename = "data_bank.csv"
    json_filename = input("введите имя файла json (пустой ввод введет data_bank.json) ").strip()
    if json_filename == "" :
        json_filename = "data_bank.json"
    date_actu = input("введите дату актуальности данных в формате дд.мм.ггг (пустой ввод введет 01.01.2021 ) ").strip()
    if date_actu == "" :
        date_actu = "01.01.2021"
    market = input("введите имя market-канала (пустой ввод введет Foreign Currency Market ) ").strip()
    if market == "" :
        market = "Foreign Currency Market"
        
    pd = R_csv()
    
    csv_list = pd.read_scv(csv_filename)
    json_str = forex_csv_2_json(csv_list)
    
    #print(json_str)
    
    file_json = open(json_filename,"w",encoding='utf-8')
    file_json.write('{\n'+4*' '+'"Data":"'+date_actu+'",\n'+4*' '+'"name":"'+market+'",\n'+4*' '+'"Valute":{\n'+json_str+4*' '+'}\n}\n')
    file_json.close()

