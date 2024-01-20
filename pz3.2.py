import datetime
class File:  # создали класс
    # создаем атрибуты
    def __init__(self, name, creation_date, filetype):
        self.__name = str(name)
        self.__creation_date = creation_date
        self.__filetype = filetype
    def set_name(self, name):
        self.__name = name.replace("#","").replace(";","").replace(".","").replace("/","").replace("\\","") #заменяем знаки на пустое поле
        self.__name = self.__name[0:25]
    def get_name(self):
        return self.__name
    def get_creation_date(self):
        return self.__creation_date
    def get_filetype(self):
        return self.__filetype
    def set_creation_date(self, creation_date):
        if creation_date<datetime.datetime.now():
            self.__creation_date = creation_date
        else:
            self.__creation_date=datetime.datetime.now() #будет выводиться сегодняшняя дата
    def set_filetype(self, filetype):
        allowed_types = ["txt", "doc", "png"] #Массив типов данных
        for type in allowed_types:
            if type == filetype:
                self.__filetype = filetype
                return
        self.__filetype = "none" #если будет некорректный тип файла, то будет NONE
        #вывод данных
file1 = File(input("Введите название файла: "),datetime.datetime(2024,1,1),input("Введите тип файла: "))
print(file1.get_name())
print(file1.get_creation_date())
print(file1.get_filetype())