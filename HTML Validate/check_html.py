class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

fname = input("Please enter HTML file name and extention: ")
with open(fname,'r') as html_file:
    data = html_file.read().replace('\n','')

def tag_check(data):
    s = Stack()
    index = 0
    balanced = True
    while index < len(data) and balanced:
        symbol = data[index]
        if symbol == '<':
            s.push(symbol)
        if symbol == '>':
            if s.isEmpty():
                return 'Invalid HTML, mismatched opening and closing braces'
            s.pop()
        index += 1
    if balanced and s.isEmpty():
        return 'Valid HTML'
    else:
        return 'Invalid HTML, mismatched opening and closing braces'
print(tag_check(data))


