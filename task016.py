#Простой класс
#Реализуйте класс Student со следующими методами:
# get_python_skill() - получить численную оценку уровня знания Python 
# learn_python() - увеличить численную оценку уровня знания Python на 1
#Изначально значение численной оценки уровня знания Python - 0.
#Пример использования: 
#s = Student() 
#s.get_python_skill()

class Student :
    def __init__(self) :
        self.python_skill = 0
        
    def learn_python(self) :
        self.python_skill += 1

    def get_python_skill(self) :
        return self.python_skill


#
if __name__ == '__main__' :
    s = Student() 
    print(s.get_python_skill())
    s.learn_python()
    print(s.get_python_skill())
    s.learn_python()
    s.learn_python()
    print(s.get_python_skill())
