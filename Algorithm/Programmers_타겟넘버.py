count=0

def dfs(idx, numbers, target, totalsum, length):
    global count
    if length==idx:
        if target==totalsum: count+=1
        return
    else:
        dfs(idx+1, numbers, target, totalsum+numbers[idx], length)
        dfs(idx+1, numbers, target, totalsum-numbers[idx], length)
        
def solution(numbers, target):
    dfs(0, numbers, target, 0, len(numbers))
    return count

if __name__ == "__main__":
    numbers=list(map(int, input().split(',')))
    target=int(input())
    print(solution(numbers, target))