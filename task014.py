#Простой итератор
#Реализуйте класс PrimesIterator, позволяющий 
#итерироваться по простым числам, начиная 
#с заданного. Примеры использования:
#for n in PrimesIterator(42): print(n)
#for n in PrimesIterator(): print(n)

#
class PrimesIterator :
    def __init__(self, ini_simple) :
        self.num_simple = ini_simple
        self.simple_list = [2,3]
        i = 4
        while i<ini_simple :
            s_simple = i
            not_break = True
            for sim in self.simple_list :
                l = divmod(s_simple, sim)
                if l[1] == 0 :
                    not_break = False
                    break
            if not_break :    
                self.simple_list.append(s_simple)
            i += 1
        
    def next_simple(self) :
        i = self.num_simple
        while i<10000000 :
            s_simple = self.num_simple + i 
            not_break = True
            for sim in self.simple_list :
                l = divmod(s_simple, sim)
                if l[1] == 0 :
                    not_break = False
                    break
            if not_break :    
                self.simple_list.append(s_simple)
                return s_simple
            i += 1
         
    def __next__(self) :
        if self.num_simple <10000000 :
            self.num_simple = self.next_simple()
            return self.num_simple
        else :
            raise StopIteration

    def __iter__(self) :
        return self
        
#
if __name__ == '__main__' :
    inp_int = int(input('введите число для начала итерации простых чисел '))
    for n in PrimesIterator(inp_int) :
        print(n)
