import random
import time

class Element:
    def __init__(self, data = None, priorytet = None):
        self.data = data
        self.priorytet = priorytet

    def __lt__(self, other):          #<
        return self.priorytet < other.priorytet

    def __ge__(self, other):            #>
        return self.priorytet > other.priorytet

    def __str__(self):      #wypisywanie printem
        return str(self.priorytet)+":"+str(self.data)


class Queue:
    def __init__(self, lista = None):
        self.size = 0
        self.list_to_sort = lista
        self.tab = []
        if lista is not None:
            for i in lista:
                self.enqueue(i.data, i.priorytet)



    def is_empty(self):
        if len(self.tab) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.tab[0]
            self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
            # self.tab.pop(len(self.tab) - 1)
            self.size = self.size - 1
            i = 0
            while i < self.size:
                ileft = self.left(i)
                iright = self.right(i)
                if iright < self.size and ileft < self.size and i < self.size:
                    if self.tab[iright].priorytet > self.tab[ileft].priorytet and self.tab[iright].priorytet > self.tab[i].priorytet:
                        self.tab[i], self.tab[iright] = self.tab[iright], self.tab[i]
                    elif self.tab[ileft].priorytet >= self.tab[iright].priorytet and self.tab[ileft].priorytet > self.tab[i].priorytet:
                        self.tab[i], self.tab[ileft] = self.tab[ileft], self.tab[i]
                elif ileft < self.size and i < self.size and iright >= self.size:
                    if self.tab[ileft].priorytet >= self.tab[i].priorytet:
                        self.tab[i], self.tab[ileft] = self.tab[ileft], self.tab[i]
                i = i +1

            return data

    def enqueue(self, data, priorytet):
        el = Element(data, priorytet)
        self.tab.append(el)
        i = len(self.tab)
        while i > 0:
            iparent = self.parent(i)
            if iparent < len(self.tab) and i < len(self.tab):
                if self.tab[i].priorytet > self.tab[iparent].priorytet:
                    self.tab[iparent], self.tab[i] = self.tab[i], self.tab[iparent]
            i = i-1
        self.size = self.size +1



    def left(self, index):
        return 2*index+1

    def right(self, index):
        return 2*index + 2

    def parent(self, index):
        return (index-1)//2

    def print_dict(self):
        if self.is_empty():
            print("{}")
        else:
            print('{', end=' ')
            for i in range(len(self.tab) - 1):
                print(self.tab[i], end=', ')
            if self.tab[len(self.tab) - 1]: print(self.tab[len(self.tab) - 1], end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx<len(self.tab):
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl+1)


    def heapify(self, id):
        pass


def test_for_heap():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    new_tab = []
    for i in tab:
        new_el = Element(i[1], i[0])
        new_tab.append(new_el)

    empty = Queue(new_tab)
    empty.print_tree(0,0)
    empty.print_dict()

    while empty.size:
        empty.dequeue()
    empty.print_tree(0,0)
    empty.print_dict()

    tab = []
    for i in range(1000):
        tab.append(int(random.random() * 100))
    new_tab = []

    for i in tab:
        new_el = Element(None, i)
        new_tab.append(new_el)

    empty = Queue(new_tab)

    t_start = time.perf_counter()
    while empty.size:
        empty.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))





def swap(tab):
    size = len(tab)
    while size > 0:
        minim = tab[len(tab) - size].priorytet
        for i in range(len(tab)-size, len(tab)):
            if tab[i].priorytet < minim:
                minim = tab[i].priorytet
                tab[len(tab)-size], tab[i] = tab[i], tab[len(tab)-size]
        size = size - 1

def print_dict(tab):
    print('{', end=' ')
    for i in range(len(tab) - 1):
        print(tab[i], end=', ')
    if tab[len(tab) - 1]: print(tab[len(tab) - 1], end=' ')
    print('}')

def test_for_swap():
    tab1 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    new_tab1 = []
    for i in tab1:
        el = Element(i[1], i[0])
        new_tab1.append(el)
    swap(new_tab1)
    print_dict(new_tab1)

    tab2 = []
    for i in range(10000):
        tab2.append(int(random.random() * 100))
    new_tab2 = []

    for i in tab2:
        new_el = Element(None, i)
        new_tab2.append(new_el)

    t_start = time.perf_counter()
    swap(new_tab2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

def shift(tab):
    size = len(tab)
    while size > 0:
        minim = tab[len(tab) - size].priorytet
        for i in range(len(tab) - size, len(tab)):
            if tab[i].priorytet < minim:
                minim = tab[i].priorytet
                najmniejsza = tab.pop(i)
                tab.insert(len(tab) - size, najmniejsza)
        size = size - 1


def test_for_shift():
    tab1 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    new_tab1 = []
    for i in tab1:
        el = Element(i[1], i[0])
        new_tab1.append(el)
    shift(new_tab1)
    print_dict(new_tab1)

    tab2 = []
    for i in range(10000):
        tab2.append(int(random.random() * 100))
    new_tab2 = []

    for i in tab2:
        new_el = Element(None, i)
        new_tab2.append(new_el)

    t_start = time.perf_counter()
    shift(new_tab2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))



if __name__ == "__main__":
    test_for_heap()
    test_for_swap()
    test_for_shift()








