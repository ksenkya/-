class File: #создали класс
    # создаем атрибуты
    def __init__(self, name, create_date, type):
        self.__name = name
        self.__create_date = create_date
        self.__type = type
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_create_date(self):
            return self.__create_date
    def set_create_date(self, create_date):
            self.__create_date = create_date
    def get_type(self):
                return self.__type
    def set_type(self, type):
                self.__type = type
#выводим наши данные
file1 = File("nazvanie.txt", "2023-01-20", "txt")
file2 = File("document1.docx", "2024-01-20", "docx")
print ("File1:")
print("Name:", file1.get_name())
print("Creation Date:", file1.get_create_date())
print("Type:",file1.get_type())
print("\n")
print ("File2:")
print("Name:", file2.get_name())
print("Creation Date:", file2.get_create_date())
print("Type:",file2.get_type())

