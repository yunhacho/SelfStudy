class Node:
    def __init__(self, data, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

class EditTable:
    def __init__(self,n,k):
        self.init_table(n,k)
        self.DeleteStack=[]

    # n개 노드 가진 이중연결리스트 초기화
    def init_table(self,n,k): 
        prev=Node(0)
        for index in range(n-1):
            # k번째 노드에 현재 위치(self.curpos) 두기
            if index==k: self.curpos=prev 
            cur=Node(index+1,prev)
            prev.next=cur; prev=cur
    
    # "U X" x번만큼 이전 노드로 옮겨 self.curpos 두기
    def forward_X_from_curpos(self, x):
        curpos=self.curpos
        for _ in range(x): curpos=curpos.prev
        self.curpos=curpos

    # "D X" x번만큼 다음 노드로 옮겨 self.curpos 두기
    def backward_x_from_curpos(self, x):
        curpos=self.curpos
        for _ in range(x): curpos=curpos.next
        self.curpos=curpos

    # "C" 현재 위치 노드 삭제 후 self.curpos 옮기기
    def delete_curpos_select_next(self):
        self.DeleteStack.append(self.curpos)
        # 현재 위치 노드가 맨 끝 노드여서 다음이 없을 때 
        # 전 노드로 self.curpos 옮김
        if self.curpos.next is None: 
            self.curpos=self.curpos.prev
            self.curpos.next=None
        else: 
            next_node=self.curpos.next
            # 현재 위치 노드가 맨 앞 노드이면 
            # 다음 노드(self.curpos가 될)의 prev None 변경
            if self.curpos.prev is None:
                next_node.prev=None
            else: # 현재 위치 노드가 앞뒤노드 다 있을 때
                  # 앞뒤노드 연결
                self.curpos.prev.next=next_node
                next_node.prev=self.curpos.prev

            self.curpos=next_node 
    
    # "Z" 삭제된 노드 스택에서 노드 가져와 되돌리기
    def bring_back_recentDelete(self):
        node_to_bringback=self.DeleteStack.pop()

        prev_node=node_to_bringback.prev
        next_node=node_to_bringback.next

        # 되돌릴 노드의 prev가 None(노드가 원래 맨앞에 있었을 때)
        # 이면 되돌릴 노드 다음 노드의 prev를 되돌릴 노드로 변경
        if prev_node is None:
            next_node.prev=node_to_bringback
        # 되돌릴 노드의 next가 None(노드가 원래 맨뒤에 있었을 때)
        # 이면 되돌릴 노드 이전 노드의 next를 되돌릴 노드로 변경
        elif next_node is None:
            prev_node.next=node_to_bringback
        else: # 앞뒤노드가 있는 경우 앞뒤노드와 되돌릴노드 연결
            prev_node.next=node_to_bringback
            next_node.prev=node_to_bringback
    
    def get_DeleteStack(self): # 삭제된 노드의 인덱스 리턴
        return [ node.data for node in self.DeleteStack]

def solution(n, k, cmd):
    answer = ['O'] * n
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
    # 삭제된 노드 인덱스만 'X'로 변경
    for index in Deleted: answer[index]='X'
    return ''.join(answer)

if __name__=="__main__":
    cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    print(solution(8,2,cmd))