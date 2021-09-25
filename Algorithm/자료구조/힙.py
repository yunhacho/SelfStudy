class Heap: # Max Heap
    def __init__(self) -> None:
        self.heap=[None]
    
    def move_up(self, insert_idx) -> bool:
        if insert_idx <=1: return False
        # Min Heap은 부등호 바꾸면 됨
        return self.heap[insert_idx//2] < self.heap[insert_idx]

    def insert(self, value):
        self.heap.append(value)
        insert_idx = len(self.heap)-1
        while self.move_up(insert_idx):
            self.heap[insert_idx//2], self.heap[insert_idx] = self.heap[insert_idx], self.heap[insert_idx//2]
            insert_idx//=2

    def move_down(self, pop_idx):
        left_child, right_child = pop_idx*2, pop_idx*2+1
        if left_child >= len(self.heap): return False, None
        elif right_child >= len(self.heap):
            if self.heap[left_child] > self.heap[pop_idx]: return True, left_child
            else: return False, None
        else:
            if self.heap[left_child] > self.heap[right_child]:
                if self.heap[left_child] > self.heap[pop_idx]: return True, left_child
            elif self.heap[right_child] > self.heap[pop_idx]: return True, right_child
        return False, None

    def pop(self):
        if len(self.heap)<=1: return None
        returned_value=self.heap[1]
        self.heap[1]=self.heap[-1]
        pop_idx=1; del self.heap[-1]
        while True:
            can_move, change_idx = self.move_down(pop_idx)
            if not can_move: break
            self.heap[change_idx], self.heap[pop_idx] = self.heap[pop_idx], self.heap[change_idx]
            pop_idx=change_idx
        return returned_value

if __name__=="__main__":
    heap=Heap()
    nums=[14,35,23,43,2,30]
    for n in nums:
        heap.insert(n)
    for i in range(len(nums)):
        print(heap.pop())
    print(heap.heap)