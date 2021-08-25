import sys

def solve_1339(words: list)->int:
  alpha={}
  for word in words: 
    for i, w in enumerate(word[::-1]):
      if w in alpha.keys(): alpha[w]+=10**i
      else: alpha[w]=10**i
  return sum(v*n for v,n in zip(sorted(alpha.values(), reverse=True), range(9,0, -1)))

if __name__=="__main__":
  n, *words = map(lambda x: x.rstrip(), sys.stdin.readlines())
  print(solve_1339(words))