class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
    
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next
        if self.sizeOfLL() <= 1:
            self.tail = self.head

    def remove_last_node(self):
        if self.head is None:
            return

        curr_node = self.head
        while (curr_node.next != None and curr_node.next.next != None):
            curr_node = curr_node.next

        curr_node.next = None
        self.tail = curr_node

    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0

        if index == 0:
            self.remove_first_node()
        else:
            while current_node is not None and position < index - 1:
                position += 1
                current_node = current_node.next

            if current_node is None or current_node.next is None:
                print("Index not present")
            else:
                current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node    

    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

        if current_node.next == None:
                self.tail = current_node     

    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
        
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next    