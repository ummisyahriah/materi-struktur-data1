#membuat stack dengan linked list
# 1. kelas Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2. Kelas Stack
class Stack:
    def __init__(self):
        self.head= None
    #method untuk menambahkan stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    #method untuk
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<-")
            temp = temp.next
        print("None")

    # method untuk menghapus stack
    def pop(self):
        if not self.head:
            return None
        temp =self.head
        self.head = self.head.next
        return temp.data
    # method untuk mencetak apakah stack kosong 
    def isEmpty(self):
        return self.head is None
    #method untuk melihat stack teratas
    def peek(self):
        if not self.head:
            return None
        return self.head.data
    
# penggunaan
mystack = Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.display()
mystack.pop()
mystack.display()
print(mystack.isEmpty())
print(mystack.peek())
    