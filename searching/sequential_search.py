# 1. Searching 25 pts
# Implement a class named SequentialStringList.
# In this class implement a method called add, that when given a string, it adds it to an internal list object.
# Next, implement a find method that takes a string as the argument. Implement the find method using sequential search. If the string is found return it, if not, return None.
# Create another class called BinaryStringList, that implements the same methods but uses a binary search as the implementation for find.
list_objects = []


class SequentialStringList:
    def add(self):
       list_objects.append(self)

    def find(self):
        pos = 0
        found = False

        while pos < len(list_objects) and not found:
            if list_objects[pos] == self:
                found = self
            else:
                pos = pos + 1