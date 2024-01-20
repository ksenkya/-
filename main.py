class STUDENT:
    def __init__(self, name, age, group, lit_marks):
        self.__name = name
        self.__age = age
        self.__group = group
        self.__lit_marks = lit_marks
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_group(self):
        return self.__group
    def set_group(self,group):
        self.__group = group
    def get_lit_marks(self):
        return self.__lit_marks
    def set_lit_marks(self,lit_marks):
        self.__lit_marks = lit_marks
    def average_grade(self):
        if len(self.__lit_marks)>0:
            return sum(self.__lit_marks)/len(self.__lit_marks)
        else:
            return 0
student1 = STUDENT("Друг", 18, "ИС(ПРО)-31", [3, 5, 3, 4, 4])
print(student1.get_name())
print(student1.get_age())
print(student1.get_group())
print(student1.get_lit_marks())
print(student1.average_grade())

