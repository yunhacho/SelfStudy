def solution(numbers, target):
    global count
    count=0
    dfs(0,0,numbers, target)
    return count

def dfs(depth, total, numbers, target):
    global count
    if depth==len(numbers):
        if total==target: count+=1
        return
    else:
        dfs(depth+1, total+numbers[depth], numbers, target)
        dfs(depth+1, total-numbers[depth], numbers, target)

if __name__ == "__main__":
    numbers=list(map(int, input().split(',')))
    target=int(input())
    print(solution(numbers, target))