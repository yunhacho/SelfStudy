import sys

class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data=data
        self.left=left
        self.right=right

def preorder(node : Node):
    print(node.data, end='')
    if node.left: preorder(tree[node.left])
    if node.right: preorder(tree[node.right])

def inorder(node : Node):
    if node.left: inorder(tree[node.left])
    print(node.data, end='')
    if node.right: inorder(tree[node.right])

def postorder(node: Node):
    if node.left: postorder(tree[node.left])
    if node.right: postorder(tree[node.right])
    print(node.data, end='')

if __name__=="__main__":
    tree={}
    for _ in range(int(input())):
        data, left, right=sys.stdin.readline().split()
        left=None if left=='.' else left
        right=None if right == '.'else right
        tree[data]=Node(data,left,right)
    preorder(tree['A']); print()
    inorder(tree['A']); print()
    postorder(tree['A'])