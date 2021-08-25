from bisect import bisect_right
def solution(N, stages):
    s, f, length, l, r = sorted(stages), [], len(stages), 0, 0
    for n in range(N):
        l+=r; r=bisect_right(s[l:],n+1)
        f.append(r/(length-l) if length>l else 0)
    return [x[0]+1 for x in sorted(enumerate(f), key=lambda x: -x[1])]