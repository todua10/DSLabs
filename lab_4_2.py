# Класс, описывающий хеш-таблицу
class HashTable():
    def __init__(self, size):
        self.__hash_table = [[] for i in range(size)]  # Разрешение коллизий методом цепочек
        self.__size = size  # Размер таблицы

    # Хеш-функция
    def __hash(self, str):
        # Прямой полиномиальный хеш
        # h = (s0 + s1k + s2k^2 + ... + snk^n) mod p
        h = 0;
        m = 1;
        k = 137
        for char in str:
            num = ord(char)
            h = (h + num * m) % self.__size
            m = (m * k) % self.__size
        return h

    # Метод добавления строки в таблицу
    def hash_string(self, str):
        self.__hash_table[self.__hash(str)].append(str)

    # Метод поиска строки
    def search(self, str):
        if str in self.__hash_table[self.__hash(str)]:
            print(f"{self.__hash(str)}: {self.__hash_table[self.__hash(str)]}")
        else:
            print(None)

    # Метод удаления строки, начинающейся на указанную букву
    def delete(self, letter):
        for i in range(self.__size):
            if self.__hash_table[i]:
                self.__hash_table[i] = [j for j in self.__hash_table[i] if j[0] != letter]

    # Метод вывода таблицы
    def show(self):
        for i in range(self.__size):
            if self.__hash_table[i]:
                print(f"{i}: {self.__hash_table[i]}")


with open("text.txt", 'r') as f:
    strings = f.read().split()

my_hash = HashTable(10 * len(strings) ** 2)

for string in strings:
    my_hash.hash_string(string)

my_hash.search("Python")

my_hash.show()