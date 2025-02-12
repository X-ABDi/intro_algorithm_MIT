class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dic = dict()

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        self.dic[x] = self.dic.pop(node.item)
        node.item = x

    def insert_first(self, x):
        node = Doubly_Linked_List_Node(x)
        node.next = self.head
        node.prev = None
        if self.head != None:
            self.head.prev = node
        else:
            self.tail = node    
        self.head = node
        self.dic[x] = node

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)
        node.prev = self.tail
        node.next = None
        if self.tail != None:
            self.tail.next = node
        else:
            self.head = node     
        self.tail = node
        self.dic[x] = node      

    def delete_first(self):
        x = None
        if self.head != None:
            x = self.head.item
            self.dic.pop(self.head.item)
            self.head = self.head.next
        if self.head != None:
            self.head.prev = None    
        return x

    def delete_last(self):
        x = None
        if self.tail != None:
            self.dic.pop(self.tail.item)
            x = self.tail.item
            self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None    
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        node1 = self.dic[x1]
        node2 = self.dic[x2]
        L2.head = node1
        L2.tail = node2
        if node1.prev == None:
            self.head = node2.next
        if node2.next == None:
            self.tail = None
        elif node1.prev != None:        
            node1.prev.next = node2.next
            node2.next.prev = node1.prev
        node1.prev = None
        node2.next = None
        node = node1
        while node != None:
            L2.dic[node.item] = node
            node = node.next
        return L2

    def splice(self, x, L2):
        node1 = self.dic[x]
        node2 = L2
        while node2 and node1:
            node = Doubly_Linked_List_Node(node1.item)
            node.next = node1.next
            node1.next = node
            node.prev = node1
            node1 = node1.next
            node2 = node2.next
            del node2.prev
        if node1.next != None:
            node1.next.prev = node1


def main():
    L = Doubly_Linked_List_Seq()
    x = input().split()
    while x:
        if x[0]=='insert_first':
            L.insert_first(int(x[1]))
        elif x[0] == 'insert_last':
            L.insert_last(int(x[1]))
        elif x[0] == 'delete_first':
            L.delete_first()
        elif x[0] == 'delete_last':
            L.delete_last()
        elif x[0] == 'remove':
            L.remove(x[1], x[2])
        elif x[0] == 'splice':
            pass
        for l in L:
            print(l, end=' ')
        print('ok')    
        x = input().split()    


main()    