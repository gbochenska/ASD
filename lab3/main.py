def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class Queue:
    def __init__(self, size = 5):
        self.size = size
        self.tab = [None for i in range(size)]
        self.index_save = 0
        self.index_show = 0

    def is_empty(self):
        if self.index_save == self.index_show:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.tab[self.index_show]
        else:
            return None

    def dequeue(self):
        if not self.is_empty():
            to_return = self.index_show
            self.index_show = self.index_show + 1
            if self.index_show == len(self.tab):
                self.index_show = 0
            return self.tab[to_return]
        else:
            return None




    def enque(self, data):
        self.tab[self.index_save] = data
        self.index_save = self.index_save + 1           #do tego momentu index_show = 0
        if self.index_save == self.size:          #po przekroczeniu index_save poza zakres tablicy, czyli rozmiar 5
            self.index_save = 0
        if self.is_empty():
            self.tab = realloc(self.tab, 2 * self.size)
            index = self.index_show
            if index + self.size < 2 * self.size:
                for i in range(1, self.size):
                     self.tab[i], self.tab[i+self.size] = None, self.tab[i]
            self.index_show += self.size
            self.size *=2


    def print_tab(self):
        return self.tab

    def print_queue(self):
        if self.is_empty():
            return []
        else:
            queue = []
            new_index_show = self.index_show
            new_index_save = self.index_show
            for i in range(self.size):
                if self.tab[i] is not None:
                    if new_index_show != self.size:
                        queue.append(self.tab[new_index_show])
                        new_index_show +=1
                    else:
                        new_index_show = 0
                        queue.append(self.tab[new_index_show])
                        new_index_show += 1
        return queue


if __name__ == "__main__":
    empty = Queue()           #tworzę pustą kolejkę
    empty.enque(1)            #wpisuję 4 dane
    empty.enque(2)
    empty.enque(3)
    empty.enque(4)
    #
    print(empty.dequeue())
    print(empty.peek())
    print(empty.print_queue())

    empty.enque(5)
    empty.enque(6)
    empty.enque(7)
    empty.enque(8)
    print(empty.print_tab())
    while not empty.is_empty():
        print(empty.dequeue())

    print(empty.print_queue())

















