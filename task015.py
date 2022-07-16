#Комплексные числа
#Перегрузка операторов
#Реализуйте класс комплексных чисел ComplexNumber, 
#которые можно складывать, умножать и сравнивать на 
#равенство с помощью операторов. 
#Пример:
#a = ComplexNumber(10, 20) b = ComplexNumber(30, 40)
# c = ComplexNumber(40, 60)
#print(a+b == c)

#
class ComplexNumber :
    def __init__(self,re,im) :
        self.re = re
        self.im = im
        
    def __eq__(self,right ) :
        return self.re == right.re and self.im == right.im

    def __add__(self,right) :
        return ComplexNumber(self.re + right.re,self.im + right.im)

#
if __name__ == '__main__' :
#    print("введите комплексное число a ")
#    a_re = int(input('вещественную чaсть '))
#    a_im = int(input('мнимую часть '))
#    print("введите комплексное число b ")
#    b_re = int(input('вещественную чaсть '))
#    b_im = int(input('мнимую часть '))
#    a = ComplexNumber(a_re, a_im)
#    b = ComplexNumber(b_re, b_im)
#    print(b == a)
    a = ComplexNumber(10, 20) 
    b = ComplexNumber(30, 40)
    c = ComplexNumber(40, 60)
    print(a+b == c)
