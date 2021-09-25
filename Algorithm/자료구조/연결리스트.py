class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self, data):
        self.head=Node(data)

    # 맨 뒤에 새로운 노드 추가
    def append_newNode(self, data):
        cur=self.head
        while cur.next is not None: cur=cur.next
        cur.next=Node(data)
     
    # 모든 노드 값 출력
    def print_AllNodes(self):
        cur=self.head
        while cur is not None: 
            print(cur.data)
            cur=cur.next
    
    # 특정 인덱스 노드 알아내기
    def get_nodeOnIndex(self, index):
        cur=self.head; idx=0
        while idx < index:
            cur=cur.next; idx+=1
        return cur
            
    # 삽입
    def insert_node(self, index, data):
        newNode=Node(data)
        if index==0:
            newNode.next=self.head
            self.head=newNode
            return
        node=self.get_nodeOnIndex(index-1)
        next_node=node.next
        node.next=newNode
        newNode.next=next_node

    # 삭제
    def delete_nodeOnIndex(self, index):
        if index==0:
            self.head=self.head.next; return
        node=self.get_nodeOnIndex(index-1)
        node.next=node.next.next

if __name__=="__main__":
    LL=LinkedList(5)
    LL.append_newNode(12)
    LL.insert_node(1,4)
    LL.print_AllNodes()