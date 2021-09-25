from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.left=self.right=None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def search(self, key) -> bool:
        return self._search_value(self.root, key)

    def _search_value(self, node, key) -> bool:
        if node is None or node.data==key:
            return node is not None
        if node.data < key:
            return self._search_value(node.left, key)
        elif node.data > key:
            return self._search_value(node.right, key)

    def insert(self, key) -> bool:
        return self._insert_value(self.root, key)

    def _insert_value(self, root, key) -> bool:
        parent=self._search_where_to_insert(root, key)
        if parent or not root:
            if root is None: root=Node(key)
            else:
                if key < parent.data: parent.left=Node(key)
                else: parent.right=Node(key)
            return True
        return False

    def _search_where_to_insert(self, root, key) -> Node:    
        parent=root
        while(root):
            parent=root
            if root.data==key: return None
            if key < root.data: root=root.left
            else: root=root.right
        return parent

    def delete(self, key) -> bool:
        pass

    def bfs(self) -> None:
        root=self.root; queue=deque()
        queue.append(root)
        while root:
            node=queue.popleft()
            print(node.data, sep=' ')
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return 
    
    def inorder(self) -> None:
        root=self.root; stack=[]
        if root is None: 
            print(root); return
        while True:
            while root: stack.append(root); root=root.left
            node=stack.pop()
            if node is None: break  
            print(node.data, sep=' ')
            root=node.right
        
            


if __name__=="__main__":
    bst=BinarySearchTree()
    for data in [1,2,3,4,5,6]: bst.insert(data)
    bst.bfs()
    print()
    bst.inorder()

