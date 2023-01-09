import polska
class Vertex:
    def __init__(self, data1, data2, key):
        self.data1 = data1
        self.data2 = data2
        self.key = key

    def __eq__(self, other):
        self.key = other.key

    def __hash__(self):
        return hash(self.key)

class Edge:
    def __init__(self, vertex1, vertex2):
        self.edge = (vertex1.key, vertex2.key)


class NMatrix:
    def __init__(self):
        self.list = []
        self.dictionary = {}
        self.nmat = [[None for i in range(16)] for k in range(16)]

    def insertVertex(self,vertex):
        self.list.append(vertex)
        for i in range(0, len(self.list)):
            if self.list[i]  is vertex:
                self.dictionary[vertex.key] = i

    def insertEdge(self, vertex1, vertex2, edge):
        vertex1_idx = self.getVertexIdx(vertex1)
        vertex2_idx = self.getVertexIdx(vertex2)
        self.nmat[vertex1_idx][vertex2_idx] = edge

    def deleteEdge(self, vertex1, vertex2, edge):
        vertex1_idx = self.getVertexIdx(vertex1)
        vertex2_idx = self.getVertexIdx(vertex2)
        self.nmat[vertex1_idx][vertex2_idx] = None
        self.nmat[vertex2_idx][vertex1_idx] = None

    def deleteVertex(self, vertex):
        for i in self.list:
            if i.key == vertex.key:
                self.list.remove(i)
                removed_idx = self.getVertexIdx(i)
                removed = self.dictionary.pop(i.key)
                for key in self.dictionary.keys():
                    if removed_idx < self.dictionary[key]:
                        self.dictionary[key] = self.dictionary[key] - 1
        for i in range(len(self.nmat[0])):
            self.nmat[i][removed_idx], self.nmat[i][removed_idx+1] = self.nmat[i][removed_idx+1], None
            self.nmat[removed_idx][i], self.nmat[removed_idx+1][i] = self.nmat[removed_idx+1][i], None


    def getVertexIdx(self, vertex):
        return self.dictionary[vertex.key]

    def getVertex(self, vertex_idx):
        for i in self.dictionary.keys():
            if self.dictionary[i] == vertex_idx:
                return i

    def neighbours(self, vertex_idx):
        list_of_neighbours = []
        for i in range(len(self.nmat)):
            if self.nmat[i][vertex_idx] is not None or self.nmat[vertex_idx][i] is not None:
                list_of_neighbours.append(i)
        return list_of_neighbours

    def order(self):
        return len(self.list)

    def size(self):
        sizee = 0
        for i in range(len(self.nmat[0])):
            for j in range(len(self.nmat[0])):
                if self.nmat[i][j] is not None:
                    sizee +=1
        return sizee

    def edges(self):
        list_pair = []
        for i in range(len(self.nmat[0])):
            for j in range(len(self.nmat[0])):
                if self.nmat[i][j] is not None:
                    begin = self.getVertex(i)
                    end = self.getVertex(j)
                    list_pair.append((begin, end))
        return list_pair


class NList:
    def __init__(self):
        self.list = []
        self.dictionary = {}
        self.nlist = [[None] for i in range(16)]

    def insertVertex(self, vertex):
        self.list.append(vertex)
        for i in range(0, len(self.list)):
            if self.list[i] is vertex:
                self.dictionary[vertex.key] = i

    def insertEdge(self, vertex1, vertex2, edge):
        id = self.getVertexIdx(vertex1)
        self.nlist[id].append(vertex2.key)
        if self.nlist[id][0] is None:
            self.nlist[id].pop(0)


    def deleteEdge(self, vertex1, vertex2, edge):
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
            i_idx = self.getVertexIdx(i)
            list_idx.append(i_idx)
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


if __name__ == "__main__":
    # empty = NMatrix()
    # vertex1 = Vertex(80, 100, 'Z')
    # vertex2 = Vertex(180, 50, 'G')
    # vertex3 = Vertex(330, 80, 'N')
    # edge1 = Edge(vertex1, vertex2)
    # edge2 = Edge(vertex1, vertex3)
    # edge3 = Edge(vertex2, vertex3)
    # empty.insertVertex(vertex1)
    # empty.insertVertex(vertex2)
    # empty.insertVertex(vertex3)
    # empty.insertEdge(vertex1, vertex2, edge1)
    # empty.insertEdge(vertex1, vertex3, edge2)
    # empty.insertEdge(vertex2, vertex3, edge3)
    # print(empty.dictionary)
    # print(empty.list)
    # empty.deleteVertex(vertex1)
    # print(empty.dictionary)
    # print(empty.list)
    # print(empty.getVertex(0))
    # print(empty.nmat)
    # print(empty.size())
    # print(empty.edges())
    graf1 = NMatrix()

    for j in polska.polska:
        j = Vertex(j[0],j[1],j[2])
        graf1.insertVertex(j)
    ver1 = None


    for i in polska.graf:
        for j in graf1.list:
            if j.key == i[0]:
                vertex1 = j
                continue
            elif j.key == i[1]:
                vertex2 = j
        graf1.insertEdge(vertex1, vertex2, 1)

    vertex1 = Vertex(polska.polska[14][0], polska.polska[14][1],polska.polska[14][2])
    graf1.deleteVertex(vertex1)

    vertex2 = Vertex(polska.polska[8][0], polska.polska[8][1],polska.polska[8][2])
    vertex3 = Vertex(polska.polska[7][0], polska.polska[7][1], polska.polska[7][2])

    graf1.deleteEdge(vertex2, vertex3, 1)
    # polska.draw_map(graf1.edges())
    # for i in graf.nmat:
    #     print(i)
    # polska.draw_map((graf.edges()))

    # nlist = [[None] for i in range(16)]
    # key = 2
    #
    # nlist[key].append(6)
    # nlist[key].append(7)
    # nlist[key].append(8)
    # if None in nlist[key]:
    #     nlist[key].pop(0)
    # nlist[key].remove(7)
    # print(nlist)

    graf = NList()

    for j in polska.polska:
        j = Vertex(j[0], j[1], j[2])
        graf.insertVertex(j)
    ver1 = None

    for i in polska.graf:
        for j in graf.list:
            if j.key == i[0]:
                vertex1 = j
                continue
            elif j.key == i[1]:
                vertex2 = j
        graf.insertEdge(vertex1, vertex2, 1)

    vertex2 = Vertex(polska.polska[8][0], polska.polska[8][1], polska.polska[8][2])
    vertex3 = Vertex(polska.polska[7][0], polska.polska[7][1], polska.polska[7][2])


    graf.deleteEdge(vertex2, vertex3, 1)
    vertex1 = Vertex(polska.polska[14][0], polska.polska[14][1], polska.polska[14][2])
    graf.deleteVertex(vertex1)
    # for i in graf.nlist:
    #     print(i)

    print(graf.nlist)
    print(graf.neighbours(1))

    # polska.draw_map(graf.edges())




