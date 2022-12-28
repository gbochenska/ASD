#nieskończone
class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size, c1 = 0, c2 = 1):
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def hash_fun(self, key):
        if isinstance(key, str):
            sum_of_letters = 0
            for i in key:
                sum_of_letters += ord(i)
            key = sum_of_letters
        return key % self.size

    def collision(self, key, index):
        # index = 0
        # i = 1
        # while i < self.size:
        #     if self.tab[i] is None:
        #         index = i
        #         print(i, index)
        #         break
        #     else:
        #         i += 1
        for i in range(self.size):
            index = (self.hash_fun(key) + self.c1 * i + self.c2 * i**2) % self.size
            if self.tab[index] is None:
                break
            else:
                index = None
        return index

    def search(self, key):
        index = self.hash_fun(key)
        result = 0
        for i in self.tab:
            if i is not None:
                if i[0] == key:
                    result =  i[1]
                    break
                else:
                    result = None
            else:
                result = None
        return result

    def insert(self, el):
        flag = 0
        for i in self.tab:
             if i is not None:
                 flag = True
             else:
                 flag = False
                 break
        if flag:
             if self.tab[self.hash_fun(el.key)][0] == el.key:
                 self.tab[self.hash_fun(el.key)][1] = el.value
             else:
                 print("Brak miejsca")
                 return None


        else:
            index = self.hash_fun(el.key)
            if self.tab[index] is None:
                self.tab[index] = [el.key, el.value]

            else:
                if  self.tab[index][0] != el.key:
                    index = self.collision(el.key, index)
                    if index is None:
                        print("Brak miejsca")
                        return None
                    else:
                        self.tab[index] = [el.key, el.value]
                else:
                    self.tab[self.hash_fun(el.key)][1] = el.value



    def remove(self, key):
        flag = 0
        for i in self.tab:
            if i is None:
                flag = True
            else:
                if i[0] == key:
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            print("Brak danej")
            return None
        else:
            index = self.hash_fun(key)
            self.tab[index] = None



    def __str__(self):
        dict = "{"
        for i in self.tab:
            if i is None:
                dict += str(None)
                dict += ", \n"
            else:
                dict += str(i[0]) + " : " + str(i[1])
                dict += ", \n"
        dict += "}"
        return str(dict)


def fun1(size, c1, c2):
    tab = HashTable(size, c1, c2)
    el1 = Element(1, 'A')
    el2 = Element(2, 'B')
    el3 = Element(3, 'C')
    el4 = Element(4, 'D')
    el5 = Element(5, 'E')
    el18 = Element(18, 'F')
    el31 = Element(31, 'G')
    el8 = Element(8, 'H')
    el9 = Element(9, 'I')
    el10 = Element(10, 'J')
    el11 = Element(11, 'K')
    el12 = Element(12, 'L')
    el13 = Element(13, 'M')
    el14 = Element(14, 'N')
    el15 = Element(15, 'O')


    tab.insert(el1)
    tab.insert(el2)
    tab.insert(el3)
    tab.insert(el4)
    tab.insert(el5)
    tab.insert(el18)
    tab.insert(el31)
    tab.insert(el8)
    tab.insert(el9)
    tab.insert(el10)
    tab.insert(el11)
    tab.insert(el12)
    tab.insert(el13)
    tab.insert(el14)
    tab.insert(el15)
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    el5z = Element(5, 'Z')
    tab.insert(el5z)
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    el_test = Element('test', 'W')
    tab.insert(el_test)
    print(tab)

def fun2(size, c1, c2):
    tab = HashTable(size, c1, c2)
    el1 = Element(13, 'A')
    el2 = Element(26, 'B')
    el3 = Element(39, 'C')
    el4 = Element(52, 'D')
    el5 = Element(65, 'E')
    el18 = Element(78, 'F')
    el31 = Element(91, 'G')
    el8 = Element(104, 'H')
    el9 = Element(117, 'I')
    el10 = Element(130, 'J')
    el11 = Element(143, 'K')
    el12 = Element(156, 'L')
    el13 = Element(169, 'M')
    el14 = Element(182, 'N')
    el15 = Element(195, 'O')


    tab.insert(el1)
    tab.insert(el2)
    tab.insert(el3)
    tab.insert(el4)
    tab.insert(el5)
    tab.insert(el18)
    tab.insert(el31)
    tab.insert(el8)
    tab.insert(el9)
    tab.insert(el10)
    tab.insert(el11)
    tab.insert(el12)
    tab.insert(el13)
    tab.insert(el14)
    tab.insert(el15)
    print(tab)







if __name__ == "__main__":
    fun1(13, 1, 0)
    fun2(13, 1, 0)
    fun2(13, 0, 1)
    fun1(13, 0, 1)

