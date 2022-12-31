#skończone
class Tree:
    def __init__(self, head = None):
        self.head = head


    def search(self, key):
        if self.head is None:
            return None
        else:
            return self.search1(self.head, key)

    def search1(self,  root, key):
        if root.key == key:
            return root.value
        elif root.key > key and root.left is not None:
            return self.search1(root.left, key)
        elif root.key < key and root.right is not None:
            return self.search1(root.right, key)


    def insert(self, key, data):
        if self.head is None:
            self.head = ChildNode(key, data)
        else:
            self.insert1(key, data, self.head)


    def insert1(self, key, data, node):
        if node is None:
            return ChildNode(key, data)
        if key < node.key:
            node.left = self.insert1(key, data, node.left)
            node.head = self.head
            return node
        elif key > node.key:
            node.right = self.insert1(key, data, node.right)
            node.head = self.head
            return node
        else:
            node.value = data
            return node


    def delete(self, key):
        if self.head is None:
            return None
        else:
            self.delete1(key, self.head)

    def delete1(self,key, root):
        if root is None:
            return root
        if key<root.key:
            root.left = self.delete1(key, root.left)
            return root
        elif key>root.key:
            root.right = self.delete1(key, root.right)
            return root
        if root.left is None and root.right is None:   #gdy nie ma dziecka
            return None
        if root.left is None and root.right is not None:        #gdy jest 1 dziecko
            return root.right
        elif root.right is None and root.left is not None:
            return root.left
        if root.left is not None and root.right is not None:       #gdy jest 2 dzieci
            parent = root
            child = root.right
            while child.left is not None:
                parent = child
                child = child.left
            if parent != root:
                parent.left = child.right
            else:
                parent.right = child.right
            root.key = child.key
            root.value = child.value
            return root


    def print(self):
        lista = self.print1(self.head)
        for i in range(len(lista)):
            lista[i] = str(lista[i][0]) + ":" + str(lista[i][1])
        return lista

    def print1(self, node):
        lista = []
        if node is not None:
            kr = (node.key, node.value)
            lista = lista + self.print1(node.left)
            lista.append(kr)
            lista = lista + self.print1(node.right)
            lista = sorted(lista)
        return lista


    def heigh(self):
        return self.heigh1(self.head)

    def heigh1(self, node):
        if node is None:
            return 0
        left = self.heigh1(node.left)
        right = self.heigh1(node.right)
        maxheigh = left
        if right > maxheigh:
            maxheigh = right
        return maxheigh+1



    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left, lvl + 5)

class ChildNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    empty = Tree()
    empty.insert(50, 'A')
    empty.insert(15, 'B')
    empty.insert(62, 'C')
    empty.insert(5, 'D')
    empty.insert(20, 'E')
    empty.insert(58, 'F')
    empty.insert(91, 'G')
    empty.insert(3, 'H')
    empty.insert(8, 'I')
    empty.insert(37, 'J')
    empty.insert(60, 'K')
    empty.insert(24, 'L')
    empty.print_tree()
    print(empty.print())

    print(empty.search(24))
    empty.insert(20, 'AA')
    empty.insert(6, 'M')
    empty.delete(62)
    empty.insert(59, 'N')
    empty.insert(100, 'P')
    empty.delete(8)
    empty.delete(15)
    empty.insert(55, 'R')
    empty.delete(50)
    empty.delete(5)
    empty.delete(24)
    print(empty.heigh())
    print(empty.print())
    empty.print_tree()


