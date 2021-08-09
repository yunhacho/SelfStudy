'''
Stack
- POP, PUSH, ISEMPTY, TOP, SIZE
'''

# 리스트로 구현
class Stack(object):
    def __init__(self, items=None):
        if items is None: self.items=[]
        else: self.items=items

    def pop(self):
        if self.items: return self.items.pop()
        else: return 'stack is empty'

    def push(self, item):
        self.items.append(item)
        return item

    def isEmpty(self):
        return not bool(self.items)

    def top(self):
        if self.items: return self.items[-1]
        else: return 'stack is empty'

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

#노드로 구현
class Node(object):
    def __init__(self, data=None, pointer=None) -> None:
        self.data=data
        self.pointer=pointer

class Stack_Node(object):
    def __init__(self) -> None:
        self.head=None
        self.count=0

    def pop(self):
        if self.head is None:
            return 'stack is empty'
        else:
            item=self.head.data
            self.head=self.head.pointer
            self.count-=1
            return item

    def push(self, item):
        self.head=Node(item, self.head)
        self.count+=1
        return item

    def isEmpty(self):
        return not bool(self.head)

    def top(self):
        if self.head: return self.head.data
        else: return 'stack is empty'

    def size(self):
        return self.count

    def print_stack(self):
        node=self.head
        while node:
            print(node.data, end=' ')
            node=node.pointer

if __name__=="__main__":
    mode='Node'
    if mode=='list':
        stack=Stack(list(range(10)))
        for _ in range(11): 
            print("pop: {}".format(stack.pop()))
        print(stack)
    elif mode=='Node':
        stack=Stack_Node()
        for n in range(10): stack.push(n)
        for _ in range(11): print("pop: {}".format(stack.pop()))
        stack.print_stack()
