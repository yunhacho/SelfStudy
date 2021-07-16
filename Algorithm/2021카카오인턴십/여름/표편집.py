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
            self.curpos.next=None
        else:
            next_node=self.curpos.next
            self.curpos.prev.next=next_node
            next_node.prev=self.curpos.prev
            self.curpos=next_node 

    def bring_back_recentDelete(self):
        node_to_bringback=self.DeleteStack.pop()
        prev_node=node_to_bringback.prev
        next_node=node_to_bringback.next

        if prev_node is None:
            next_node.prev=node_to_bringback
        elif next_node is None:
            prev_node.next=node_to_bringback
        else:
            prev_node.next=node_to_bringback
            next_node.prev=node_to_bringback
    
    def get_DeleteStack(self):
        return [ node.data for node in self.DeleteStack]

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    edit=EditTable(n,k)
    for command in cmd:
        cmdlist=command.split()
        if cmdlist[0]=='D':
            edit.backward_x_from_curpos(int(cmdlist[1]))
        elif cmdlist[0]=='U':
            edit.forward_X_from_curpos(int(cmdlist[1]))
        elif cmdlist[0]=='C':
            edit.delete_curpos_select_next()
        elif cmdlist[0]=='Z':
            edit.bring_back_recentDelete()

    Deleted=edit.get_DeleteStack()
    for index in Deleted: answer[index]='X'
    return ''.join(answer)

if __name__=="__main__":
    cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    print(solution(8,2,cmd))