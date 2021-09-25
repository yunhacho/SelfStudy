class Node:
    def __init__(self, data, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoubleLinkedList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None, self.head)
        self.head.next=self.tail
        self.size=0
    
    def is_empty(self):
        return not self.size
    
    def append_left(self, value):
        if self.is_empty():
            self.head=Node(value)
            self.tail=Node(None,self.head)
            self.head.next=self.tail
        else:
            head=self.head
            self.head=Node(value, None, self.head)
            head.prev=self.head
        self.size+=1
    
    def append(self, value):
        if self.is_empty():
            self.head=Node(value)
            self.tail=Node(None, self.head)
            self.head.net=self.tail
        else:
            node=Node(value, self.tail)
            self.tail.next=node
            node=self.tail
        self.size+=1
    
    def insert(self, value, idx):
        if idx < self.size//2:
            pass