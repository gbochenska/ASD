
class ListItem:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, el):
        newel = ListItem(el)
        newel.next = self.head
        self.head = newel

    def remove(self):
        self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        length = 1
        next = self.head.next
        while next is not None:
            length += 1
            next = next.next
        return length

    def get(self):
        return self.head.value

    def listprint(self):
        val = self.head
        while val is not None:
            print(val.value)
            val = val.next

    def add_end(self, el):
        newel = ListItem(el)
        if self.head is None:
            self.head = newel
        i = self.head
        while i.next is not None:
            i = i.next
        i.next = newel

    def remove_end(self):
        if self.head.next is None:
            self.head = None
        i = self.head
        while i.next.next is not None:
            i = i.next
        last = i.next
        i.next = None
        last = None

    def take(self, n):
        if self.length() > n:
            new_list = Linkedlist()
            el = self.head
            new_list.add(el.value)
            for i in range(n-1):
                el = el.next
                new_list.add_end(el.value)
        else:
            new_list = Linkedlist()
        return  new_list

    def drop(self, n):
        if self.length() > n:
            new_list = Linkedlist()
            el = self.head
            for i in range(n):
                el = el.next
            new_list.add(el.value)
            for i in range(n+1, self.length()):
                el = el.next
                new_list.add_end(el.value)
        else:
            new_list = Linkedlist()
        return  new_list




if __name__ == "__main__":

    lista = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
    list = Linkedlist()
    e1 = ListItem(lista[0])
    e2 = ListItem(lista[1])
    e3 = ListItem(lista[2])
    e4 = ListItem(lista[3])
    e5 = ListItem(lista[4])
    e6 = ListItem(lista[5])

    list.head = e2
    list.add(lista[1])
    list.remove()
    list.add(lista[0])
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6
    list.remove_end()
    list.add_end(lista[5])

    list.listprint()

    print("Czy lista jest pusta? ", list.is_empty())

    print("Jaka jest długość listy? ", list.length())

    print("Jaki jest pierwszy element listy? ", list.get())

    print("Nowa lista wiązana stworzona z 3 pierwszych elementów listy poprzedniej: ")
    list.take(3).listprint()

    print("Nowa lista wiązana stworzona z pominięciem 3 pierwszych elementów listy poprzedniej: ")
    list.drop(3).listprint()



