from itertools import combinations

for case in list(combinations(nums, 3)):
    case=sum(case)
    isprime=True; count=0
    for i in range(2, case//2):
        if(case%i==0):
            isprime=False; break
    if isprime: count+=1

    

