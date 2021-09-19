n=input()
print('LUCKY') if sum(int(x) for x in n[:len(n)//2]) == sum(int(x) for x in n[len(n)//2:]) else print('READY')