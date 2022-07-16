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
def forex_csv_2_xml(csv_list) :
    st = ""
    key_list = csv_list[0]
    for cont_list in  csv_list[1:]:
        st0 = ""
        body0 = ""
        for key0,cont0 in zip(key_list,cont_list) :
            if key0 == "Valute":
                continue       
            elif key0 == "ID" :
                 st0 = 4*' '+'<Valute '+key0+'="'+cont0+'">\n'   
            else :
                body0 += 8*" "+"<"+key0+">"+cont0+"</"+key0+">\n" 
        st += st0+body0+4*" "+"</Valute>\n"
    return st

#
if __name__ == '__main__':
    csv_filename = input("введите имя файла csv (пустой ввод введет data_bank.csv) ").strip()
    if csv_filename == "" :
        csv_filename = "data_bank.csv"
    xml_filename = input("введите имя файла xml (пустой ввод введет data_bank.xml) ").strip()
    if xml_filename == "" :
        xml_filename = "data_bank.xml"
    date_actu = input("введите дату актуальности данных в формате дд.мм.гггг (пустой ввод введет 01.01.2021 ) ").strip()
    if date_actu == "" :
        date_actu = "01.01.2021"
    market = input("введите имя market-канала (пустой ввод введет Foreign Currency Market ) ").strip()
    if market == "" :
        market = "Foreign Currency Market"
    
    pd = R_csv()
    
    csv_list = pd.read_scv(csv_filename)
    xml_str = forex_csv_2_xml(csv_list)
    
#    print(xml_str)
    
    file_xml = open(xml_filename,"w",encoding='utf-8')
    file_xml.write('<ValCurs Data="'+date_actu+'" name="'+market+'">\n'+xml_str+'</ValCurs>\n')
    file_xml.close()

