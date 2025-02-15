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

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)
        node.prev = self.tail
        node.next = None
        if self.tail != None:
            self.tail.next = node
        else:
            self.head = node     
        self.tail = node

    def delete_first(self):
        x = None
        if self.head != None:
            x = self.head.item
            self.head = self.head.next
        if self.head != None:
            self.head.prev = None    
        return x

    def delete_last(self):
        x = None
        if self.tail != None:
            x = self.tail.item
            self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None    
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if x1.prev == None:
            self.head = x2.next
        if x2.next == None:
            self.tail = x1.prev
        elif x1.prev != None:        
            x1.prev.next = x2.next
            x2.next.prev = x1.prev
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        node = L2.head
        last = x.next
        while node :
            x.next = node
            node.prev = x
            node = node.next
            x = x.next
        x.next = last
        if last != None:
            last.prev = x
        else:
            self.tail = x    


# def main():
#     L = Doubly_Linked_List_Seq()
#     x = input().split()
#     while x:
#         if x[0]=='insert_first':
#             L.insert_first(int(x[1]))
#         elif x[0] == 'insert_last':
#             L.insert_last(int(x[1]))
#         elif x[0] == 'delete_first':
#             L.delete_first()
#         elif x[0] == 'delete_last':
#             L.delete_last()
#         elif x[0] == 'remove':
#             L.remove(x[1], x[2])
#         elif x[0] == 'splice':
#             pass
#         for l in L:
#             print(l, end=' ')
#         print('ok')    
#         x = input().split()    


# main()    