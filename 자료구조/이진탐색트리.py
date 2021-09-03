class Node:
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.head=None

    def insert(self, value):
        if not self.head: self.head=Node(value)
        else:
            current_node = self.head
            while current_node:
                parent_node=current_node
                if current_node.value == value: break
                elif current_node.value > value: current_node=current_node.left
                else: current_node = current_node.right
            if parent_node.value > value: parent_node.left=Node(value)
            else: parent_node.right=Node(value)

    def search(self, value):
        current_node=self.head
        while current_node:
            if current_node.value==value: return True
            elif current_node.value > value: current_node = current_node.left
            else: current_node = current_node.right
        return False

    def delete(self, value):
        if self.head.value == value: 
            self.head=None; return True
        searched=False
        parent_node, current_node = self.head, self.head
        while current_node:
            if current_node.value == value: searched=True; break
            parent_node = current_node
            current_node = current_node.left if current_node.value > value else current_node.right
        if not searched: return False

        # 삭제할 노드가 leaf node
        if not current_node.left and not current_node.right:
            if parent_node.value > value: parent_node.left=None
            else: parent_node.right=None
        # 삭제할 노드가 child 2개 가짐
        elif current_node.left and current_node.right:
            change_node_parent, change_node = current_node.right, current_node.right
            while change_node.left:
                change_node_parent, change_node = change_node, change_node.left
            change_node_parent.left = change_node.right if change_node.right else None
            if parent_node.value > value:
                parent_node.left = change_node
            else: parent_node.right = change_node
            change_node.left, change_node.right = current_node.left, current_node.right
        # 삭제할 노드가 child 1개 가짐
        else:
            if parent_node.value > value:
                parent_node.left = current_node.left if current_node.left else current_node.right
            else: parent_node.right = current_node.left if current_node.left else current_node.right
        return True
    
    def print(self):
        current_node = self.head
        stack=[]
        while True:
            while current_node:
                stack.append(current_node)
                current_node=current_node.left
            if not stack: break
            node=stack.pop()
            print(node.value, end=' ')
            current_node=node.right

if __name__=="__main__":
    nums=[3,15,37,52,4,13,36,28,20,22,11]
    BST=BinarySearchTree()
     
    for n in nums:
         BST.insert(n)
    for n in [52, 36, 13, 20]:
        BST.delete(n)
    for n in nums:
         if not BST.search(n): print('search failed', n)
    BST.print()
