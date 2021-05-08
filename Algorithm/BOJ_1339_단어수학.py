alpha={}; result=0; score=9
for _ in range(int(input())):
  idx=1
  for w in input()[::-1]:
    if w in alpha.keys(): alpha[w]+=idx
    else: alpha[w]=idx
    idx*=10
  
alphadic=sorted(list(alpha.items()), key=lambda x: -x[1])
for alphabet, count in alphadic:
  result+=count*score
  score-=1
print(result)