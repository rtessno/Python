# 1. Searching 25 pts
# Implement a class named SequentialStringList.
# In this class implement a method called add, that when given a string, it adds it to an internal list object.
# Next, implement a find method that takes a string as the argument. Implement the find method using sequential search. If the string is found return it, if not, return None.
list_object = []

class BinaryStringList:
    def binary_search(item):
        first = 0
        last = len(list_object) - 1
        found = False
        while first <= last and not found:
            mid_point = (first + last) // 2
            if list_object[mid_point] == item:
                found = True
            else:
                if item < list_object[mid_point]:
                    last = mid_point - 1
                else:
                    first = mid_point + 1
        return found


