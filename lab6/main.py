import random
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
    def __init__(self):
        self.tab = []

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
            self.tab[0], self.tab[-1] = self.tab[-1], self.tab[0]
            self.tab.pop(len(self.tab)-1)
            i = 0
            while i < len(self.tab):
                ileft = self.left(i)
                iright = self.right(i)
                if iright < len(self.tab) and ileft < len(self.tab) and i < len(self.tab):
                    if self.tab[iright].priorytet >= self.tab[ileft].priorytet:
                        self.tab[i], self.tab[iright] = self.tab[iright], self.tab[i]
                        break
                    else:
                        self.tab[i], self.tab[ileft] = self.tab[ileft], self.tab[i]
                elif ileft < len(self.tab) and i < len(self.tab) and iright >= len(self.tab):
                    self.tab[i], self.tab[ileft] = self.tab[ileft], self.tab[i]
                elif ileft >= len(self.tab) and iright < len(self.tab):  # Gdy jest tylko prawe dziecko
                    self.tab[i], self.tab[iright] = self.tab[iright], self.tab[i]


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
            i = i - 1


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



if __name__ == "__main__":
    # empty = Queue()
    # for i in range(len([4,7,6,7, 5,2,2,1])):
    #     n = [4,7,6,7,5,2,2,1]
    #     a = "ALGORYTM"
    #     empty.enqueue(a[i], n[i])
    # empty.print_tree(0, 0)
    # empty.print_dict()
    # print(empty.dequeue())
    # print(empty.peek())
    # empty.print_dict()
    # empty.print_tree(0,0)
    # while empty.tab:
    #     print(empty.dequeue())
    # empty.print_dict()

    tab = []
    for i in range(10):
        tab.append(int(random.random() * 100))
    new_tab = []

    for i in tab:
        new_el = Element(None, i)
        new_tab.append(new_el)
    empty = Queue()
    for i in range(len([4, 7, 6, 7, 5, 2, 2, 1])):
        n = [4, 7, 6, 7, 5, 2, 2, 1]
        a = "ALGORYTM"
        empty.enqueue(a[i], n[i])
    empty.print_tree(0, 0)
    empty.print_dict()
    print(empty.dequeue())
    print(empty.peek())
    empty.print_dict()
    empty.print_tree(0, 0)
    while empty.tab:
        print(empty.dequeue())
    empty.print_dict()



