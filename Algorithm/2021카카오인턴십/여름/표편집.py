def solution(n, k, cmd):
    answer = ''
    return answer

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

class EditTable:
    def __init__(self,n,k):
        self.init_table(n,k)
        self.DeleteStack=[]

    def init_table(self,n,k):
        prev=Node(0)
        for index in range(n-1):
            if index==k: self.curpos=prev
            cur=Node(index+1,prev)
            prev.next=cur; prev=cur
        
    def forward_X_from_curpos(self, x):
        curpos=self.curpos
        for _ in range(x): curpos=curpos.prev
        self.curpos=curpos

    def backward_x_from_curpos(self, x):
        curpos=self.curpos
        for _ in range(x): curpos=curpos.next
        self.curpos=curpos

    def delete_curpos_select_next(self):
        self.DeleteStack.append(self.curpos)
        if self.curpos.next is None:
            self.curpos=self.curpos.prev
        else:
            next_node=self.curpos.next
            self.curpos.prev.next=next_node
            next_node.prev=self.curpos.prev
            self.curpos=next_node

    def bring_back_recentDelete(self):
        node_to_bringback=self.DeleteStack.pop()
        prev_node=node_to_bringback.prev
        next_node=node_to_bringback.next

        #### case 검사 - prev 노드가 마지막인지 등등
        pass