N=int(input())
count=0
nums=[0]*(N+1)
for n in range(2, N+1):
    if nums[n]==0: 
        count+=1
        for j in range(n, N+1, n):
            nums[j]=1

print(count)