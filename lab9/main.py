class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        self.key = other.key

    def __hash__(self):
        return hash(self.key)

class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.edge = (vertex1.key, vertex2.key, weight)


class NList:
    def __init__(self):
        self.list = []
        self.dictionary = {}
        self.nlist = [[None] for i in range(10)]

    def insertVertex(self, vertex):
        self.list.append(vertex)
        for i in range(0, len(self.list)):
            if self.list[i] is vertex:
                self.dictionary[vertex.key] = i

    def insertEdge(self, vertex1, vertex2, edge):
        id1 = self.getVertexIdx(vertex1)
        if (vertex2.key, edge) not in self.nlist[id1]:
            self.nlist[id1].append((vertex2.key, edge))

        if self.nlist[id1][0] is None:
            self.nlist[id1].pop(0)




    def deleteEdge(self, vertex1, vertex2, weight):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        for i in self.nlist[idx1]:
            if i == vertex2.key:
                self.nlist[idx1].remove(i)
        for j in self.nlist[idx2]:
            if j == vertex1.key:
                self.nlist[idx2].remove(j)

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        del self.nlist[idx]
        for i in self.nlist:
            if vertex.key in i:
                i.remove(vertex.key)
        for i in self.list:
            if i.key == vertex.key:
                self.list.remove(i)
                removed_idx = self.getVertexIdx(i)
                removed = self.dictionary.pop(i.key)
                for key in self.dictionary.keys():
                    if removed_idx < self.dictionary[key]:
                        self.dictionary[key] = self.dictionary[key] - 1

    def getVertexIdx(self, vertex):
        return self.dictionary[vertex.key]

    def getVertex(self, vertex_idx):
        for i in self.dictionary.keys():
            if self.dictionary[i] == vertex_idx:
                return i

    def neighbours(self, vertex_idx):
        list_idx = []
        for i in self.nlist[vertex_idx]:
            if i is not None:
                i_w = i[1]
                i = Vertex(i[0])
                i_idx = self.getVertexIdx(i)
                list_idx.append((i_idx, i_w))
        return list_idx

    def order(self):
        return len(self.list)

    def size(self):
        edges = 0
        for i in self.nlist:
            len1 = len(i)
            edges += len1
        return edges

    def edges(self):
        pairs = []
        for i in range(len(self.nlist)):
            first_key = self.getVertex(i)
            for j in self.nlist[i]:
                second_key = j
                pair = (first_key, second_key)
                pairs.append(pair)
        return pairs

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def minKey(g, key, mstSet):
    min = float('inf')

    for v in range(len(g.nlist)):
        min_index = 0
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
        return min_index

def prima(g, s): #g - graf, a-funkcja wag krawędzi, s-wierzchołek startowy
    distance = [float('inf') for u in range(len(g.nlist))]  # zbiór wag krawędzi
    parent = [-1 for u in range(len(g.nlist))]  # poprzednik wierzchołka
    intree = [0 for u in range(len(g.nlist))]          #czy wierzchołek w drzewie
    #parent[0] = -1

    mst = NList()
    vert = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in vert:
        vertt = Vertex(i)
        mst.insertVertex(vertt)

    id = g.getVertexIdx(s)

    length = 0
    while intree[id] == 0:
        u = minKey(mst, distance, intree)

        intree[id] = 1
        for v in  g.neighbours(id):
            if distance[v[0]] > v[1]:
                distance[v[0]] = v[1]
                parent[v[0]] = g.getVertex(id)


        minim = float('inf')
        for i in range(len(g.list)):
            if distance[i] < minim and intree[i] == 0:
                minim = distance[i]
                id = i
        if minim != float('inf'):
            length += minim

        mst.insertEdge(Vertex(parent[id]), Vertex(g.getVertex(id)), distance[id])
        mst.insertEdge(Vertex(g.getVertex(id)), Vertex(parent[id]), distance[id])

    return mst




if __name__ == "__main__":
    vert = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]

    new_graf = NList()


    for i in vert:
        vertt = Vertex(i)
        new_graf.insertVertex(vertt)


    for i in graf:
        for j in new_graf.list:
            if j.key == i[0]:
                vertex1 = j
                continue
            elif j.key == i[1]:
                vertex2 = j
        new_graf.insertEdge(vertex1, vertex2, i[2])
        new_graf.insertEdge(vertex2, vertex1, i[2])

    # for i in range(len(new_graf.list)):
    #     print(new_graf.list[i].key)
    # print(new_graf.nlist)
    # printGraph(new_graf)
    mst = prima(new_graf, Vertex('A'))
    printGraph(mst)



