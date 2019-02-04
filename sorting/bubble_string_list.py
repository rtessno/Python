# Implement a class named BubbleStringList.
# In this class implement a method called add, that when given a string, it adds it to an internal list object.
# You can use the list object from the standard python library for the internal list.
# Next, implement a sort method that uses a BubbleSort to sort the list when called.
# Create another class called MergeStringList, that implements
# the same methods but uses a Merge Sort as the sorting algorithm. Create another
# class called QuickStringList that implements the same methods but used a
# QuickSort algorithm.

#  Write a test class for each and use timeit to getting
# the run times and compare the results. In your discussion, include analysis
# of the time complexity, i.e Big O.
import  timeit

obj_list = []

class BubbleStringList:
    def add(self):
        obj_list.append(self)

    def sort_obj(self):
        for passnum in range( len(self) -1, 0, -1):
            for i in range(passnum):
                if self[i] > self[i + 1]:
                    temp = self[i]
                    self[i] = self[i + 1]
                    self[i + 1] = temp

class MergeStringList:
    def mergeSort(self):
        if len(self) > 1:
            mid = len(self) // 2
            lefthalf = self[:mid]
            righthalf = self[mid:]

            MergeStringList.mergeSort(lefthalf)
            MergeStringList.mergeSort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    self[k] = lefthalf[i]
                    i = i + 1
                else:
                    self[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                self[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                self[k] = righthalf[j]
                j = j + 1
                k = k + 1

class QuickStringList:
    def quickSort(self):
        QuickStringList.quickSortHelper(self, 0, len(self) - 1)

    def quickSortHelper(self, first, last):
        if first < last:
            splitpoint = QuickStringList.partition(self, first, last)

            QuickStringList.quickSortHelper(self, first, splitpoint - 1)
            QuickStringList.quickSortHelper(self, splitpoint + 1, last)

    def partition(self, first, last):
        pivotvalue = self[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and self[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while self[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = self[leftmark]
                self[leftmark] = self[rightmark]
                self[rightmark] = temp

        temp = self[first]
        self[first] = self[rightmark]
        self[rightmark] = temp

        return rightmark
# obj_list = ['Victor', 'Zulu', 'Charlie', 'Mike', 'Whiskey', 'Quebec', 'Golf', 'Papa', 'Juliet', 'Kilo', 'Yankee', 'Delta', 'November', 'Oscar', 'India', 'Foxtrot', 'Romeo', 'Alpha', 'Tango', 'Uniform', 'Sierra', 'Echo', 'X-ray', 'Lima', 'Bravo']
# # alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# # QuickStringList.quickSort(alist)
# # print(alist)
# BubbleStringList.sort_obj(obj_list)
# print(obj_list)
