import string


# Класс, описывающий хеш-таблицу
class HashTable():
    def __init__(self):
        self.__hash_table_rus = [0 for i in range(64)]  # Список с русскими буквами
        self.__hash_table_eng = [0 for i in range(58)]  # Список с английскими буквами

    # Хеш-функция
    def __hash(self, letter):
        num = ord(letter)
        if num >= 1040:
            # True - русский, False - английский
            return num - ord('А'), True
            # Хеш буквы и язык
        else:
            return num - ord('A'), False
            # Хеш буквы и язык

    # Метод добавления буквы
    def hash_string(self, string):
        for letter in string:
            num, flag = self.__hash(letter)
            if flag:  # Если True, добавляем в список с русскими буквами
                self.__hash_table_rus[num] += 1  # Количество вхождений
            else:
                self.__hash_table_eng[num] += 1  # Количество вхождений

    # Метод поиска буквы в таблице
    def search(self, letter):
        num, flag = self.__hash(letter)
        if flag:
            print(f"{chr(num + ord('А'))}: {self.__hash_table_rus[num]}")
        else:
            print(f"{chr(num + ord('A'))}: {self.__hash_table_eng[num]}")

    # Метод вывода таблиц
    def show(self):
        for elem in range(64):
            print(f"{chr(elem + ord('А'))}: {self.__hash_table_rus[elem]}")
        for elem in range(58):
            if chr(elem + ord('A')) in string.ascii_letters:
                print(f"{chr(elem + ord('A'))}: {self.__hash_table_eng[elem]}")


my_hash = HashTable()
my_hash.hash_string("AAsssqqwppssыыйфззззйжжжятттфттц")
my_hash.show()
print()
my_hash.search('т')
