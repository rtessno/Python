### myset.py
### A set cannot have duplicates

def main():
    
    # make a small set by passing a list to set() function
    nums = set([6, 8, 3, 5, 8])
    print('Size of set is',len(nums))           # size = 4 because 2nd 8 is ignored
    print(nums)                                 # crudely dumps nums set inside { }

    nums.add(4)                                 # adds 4 to nums
    nums.update([2, 7, 5])                      # use update to add a group

    for n in nums:
        print(n,end=' ')                        # better way to view set elements

    print()

    nums.update(['abcde'])                        # adding with a string
    for n in nums:
        print(n,end=' ')                        # set types can be mixed

    print()
    print(nums)                                 # crudely dumps nums set inside { }


main()

