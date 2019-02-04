import timeit
import binary_trees
class BinaryTreeStringList:
    class Node:
        """
        Tree node: left and right child + data which can be any object
        """
        def __init__(self, data):
            """
            Node constructor

            @param data node data object
            """
            self.left = None
            self.right = None
            self.data = data

        def add(self, data):
            """
            Insert new node with data

            @param data node data object to insert
            """
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = BinaryTreeStringList.Node(data)
                    else:
                        self.left.add(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = BinaryTreeStringList.Node(data)
                    else:
                        self.right.add(data)
            else:
                self.data = data

        def find(self, data, parent=None):
            """
            Lookup node containing data

            @param data node data object to look up
            @param parent node's parent
            @returns node and node's parent if found or None, None
            """
            if data < self.data:
                if self.left is None:
                    return None, None
                return self.left.find(data, self)
            elif data > self.data:
                if self.right is None:
                    return None, None
                return self.right.find(data, self)
            else:
                return self, parent

        def print_tree(self):
            """
            Print tree content inorder
            """
            if self.left:
                self.left.print_tree()
            print(self.data,)
            if self.right:
                self.right.print_tree()

arrlist = ['Victor','Zulu','Charlie','Mike','Whiskey','Quebec', 'Golf','Papa',
          'Juliet', 'Kilo','Yankee','Delta','November',
          'Oscar','India', 'Foxtrot','Romeo','Alpha',
          'Tango','Uniform','Sierra', 'Echo', 'X-ray',
          'Lima', 'Bravo']
root = BinaryTreeStringList.Node(0)

for i in arrlist:
    root.add(i)

# root.print_tree()



t = timeit.Timer("root.find('Yankee')", "from __main__ import root")
results = t.repeat(5, 10)
for i, item in enumerate(results):
    print(i, "\t", item)
