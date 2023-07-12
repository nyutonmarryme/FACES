#определение вершины бинарного дерева,
#в инициализатор передаются данные для вершины
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    #методы для удаления, добавления вершин и отображения дерева
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

    def __find(self, node, parent, value):
        

        s, p, fl_find = self.__find(self.root, None, obj.data)

