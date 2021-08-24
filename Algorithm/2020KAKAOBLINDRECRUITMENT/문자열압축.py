def solution(s):
    answer = len(s)
    print(s)
    for unit in range(1, len(s)//2+1):
        count=1; word=s[:unit]; res='' 
        for i in range(unit, len(s)+1, unit):
            if word==s[i:i+unit]: count+=1
            else: 
                res+=str(count)+word if count>1 else word
                count=1; word=s[i:i+unit]
        res+=s[i:]
        answer=min(answer, len(res)) 
    return answer

print(solution("aabbaccc"))