def solution(answers):
    s1=[1, 2, 3, 4, 5]
    s2=[2, 1, 2, 3, 2, 4, 2, 5]
    s3=[ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    c1,c2,c3=0,0,0
    
    for i, answer in enumerate(answers):
        if s1[i%len(s1)]==answer: c1+=1
        if s2[i%len(s2)]==answer: c2+=1
        if s3[i%len(s3)]==answer: c3+=1

    return sorted([i+1 for i, c in enumerate([c1,c2,c3]) if max(c1,c2,c3)==c])