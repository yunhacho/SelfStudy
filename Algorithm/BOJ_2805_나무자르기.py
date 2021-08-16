from sys import stdin

def get_length_of_trees(heigth_of_cutter: int) -> int:
    length=0
    for tree in trees: 
        if tree>heigth_of_cutter: length+=tree-heigth_of_cutter
    return length

def get_max_length_of_trees_to_home(least_length: int) -> int:
    left, right = 1, max(trees)
    max_length=0
    while left <= right:
        mid=(left+right)//2
        if get_length_of_trees(mid) >= least_length:
            max_length=max(mid, max_length); left=mid+1
        else: right=mid-1
    return max_length

if __name__=="__main__":
    N, M = map(int, stdin.readline().split())
    trees=sorted(map(int, stdin.readline().split()))
    print(get_max_length_of_trees_to_home(M))