from itertools import combinations

N, K=list(map(int, input().split()))
cards=list(map(int, input().split()))
sortlst=[]
for tup in combinations(cards, 3): sortlst.append(sum(tup))
sortlst=list(set(sortlst))
sortlst.sort(reverse=True)
print(sortlst[K-1])
