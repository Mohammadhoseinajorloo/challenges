# 7.Write a Python program to create a class representing a linked list data structure.Include methods for displaying linked list data, inserting and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insertatbegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        else:
            new_node.next = self.head
            self.head = new_node 

    def insertatindex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self._insertatbegin(data)
        else:
            while(current_node != None and position+1 != index):
                position += 1 
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                raise Exception('index not present')

    def insertatend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node


    def updatenode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position+1 != index):
                position += 1 
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                raise Exception('index not present')

    def removefirstnode(self):
        if (self.head == None):
            return
        
        self.head = self.head.next

    def removelastnode(self):
        if self.head == None:
            return 

        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None


    def removeindexnode(self, index):
        if self.head == None:
            return 

        current_node = self.head
        position = 0
        if position == index:
            self.removefirstnode()
        else:
            while(current_node != None and position+1 != index):
                position += 1 
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                raise Exception('index not present')


    def removenode(self, data):
        current_node = self.head
    
        # Check if the head node contains the specified data
        if current_node.data == data:
            self.remove_first_node()
            return
    
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next
    
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def size(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size += 1 
                current_node = current_node.next
            return size
        else:
            return 0


    def __repr__(self):
        _str = ''
        current_node = self.head
        while(current_node.next):
            _str += f'{current_node.data}|next -> '
            current_node = current_node.next
        else:
            _str += f'{current_node.data}'
        return _str

if __name__ == '__main__':
    linklist = LinkList()
    linklist.insertatbegin(100)
    linklist.insertatbegin(90)
    linklist.insertatbegin(200)
    linklist.insertatindex(500, 1)
    linklist.insertatindex(10, 3)
    linklist.insertatend(5)
    linklist.updatenode(56, 0)
    linklist.updatenode('hello', 4)
    linklist.removefirstnode()
    linklist.removelastnode()
    linklist.removeindexnode(3)
    print(linklist.size())
    print(linklist)
