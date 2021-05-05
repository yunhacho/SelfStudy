n=int(input())
mathscore=list(map(int, input().split()))

studentdic={}
for i, score in enumerate(mathscore):
    if score not in studentdic.keys():
        studentdic[score]=i+1

average=round(sum(mathscore)/n)
mathscore=list(set(mathscore))
mathscore.sort(reverse=True)

diff=100000000
for score in mathscore:
    if abs(average-score) < diff:
        student=studentdic[score]
        diff=abs(average-score)
    else: 
        break

print(average, " ", student)