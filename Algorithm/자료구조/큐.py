'''
Queue
- Enqueue, Dequeue isEmpty, front, size
'''

# 리스트로 구현
from typing import Deque


class Queue(object):
    def __init__(self) -> None:
        self.in_stack=[]
        self.out_stack=[]

    def enqueue(self, item):
        self.in_stack.append(item)
        return item

    def dequeue(self):
        if not self.out_stack: self._transfer()
        if self.out_stack: return self.out_stack.pop()
        else: return 'queue is empty'
    
    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def isEmpty(self):
        return not bool(self.in_stack or self.out_stack)

    def front(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack: return self.out_stack[-1]
        else: return 'queue is empty'

    def size(self):
        return len(self.in_stack)+len(self.out_stack)

    def __repr__(self):
        if not self.out_stack: self._transfer()
        if self.out_stack: return repr(self.out_stack[::-1])
        else: return 'queue is empty'


#노드로 구현
class Node(object):
    def __init__(self, data=None, pointer=None) -> None:
        self.data=data
        self.pointer=pointer

class LinkedQueue(object):
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.count=0

    def enqueue(self, item):
        node=Node(item)
        if self.head is None:
            self.head=node
            self.tail=node
        else: 
            self.tail.pointer=node
            self.tail=node
        self.count+=0
        return item

    def dequeue(self):
        if self.head:
            data=self.head.data
            self.head=self.head.pointer
            self.count-=1
            return data
        else: return 'queue is empty'
    
    def isEmpty(self):
        return not bool(self.head)

    def front(self):
        if self.head: return self.head.data
        else: return 'queue is empty'

    def size(self):
        return self.count()

    def print_queue(self):
        node=self.head
        while node:
            print(node.data, end=' ')
            node=node.pointer

if __name__=="__main__":
    mode='Node'
    if mode=='list':
        queue=Queue()
        for n in range(11): 
            print("enqueue: {}".format(queue.enqueue(n)))
        print(queue); print("front of queue: {}".format(queue.front()))
        for _ in range(11):
            print("dequeue: {}".format(queue.dequeue()))
        print(queue)

    elif mode=='Node':
        queue=LinkedQueue()
        for n in range(10): print("enqueue: {}".format(queue.enqueue(n)))
        queue.print_queue(); print("front: {}".format(queue.front()))
        for _ in range(11): print("dequeue: {}".format(queue.dequeue()))
        queue.print_queue()