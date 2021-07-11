def solution(places):
    answer = []
    for place in places: answer.append(DoesHavingDistance(place))
    return answer

def IndexOfP(waitingmap):
    Index_of_P=[]
    for IndexOfRow, Row in enumerate(waitingmap):
        index=-1
        while True:
            index=Row.find('P', index+1)
            if index==-1: break
            else: Index_of_P.append([IndexOfRow, index])
    return Index_of_P

def DoesHavingDistance(waitingmap):
    Index_Of_P=IndexOfP(waitingmap)
    for Idx, P in enumerate(Index_Of_P):
        for OtherP in Index_Of_P[Idx+1:]:
            dx=P[0]-OtherP[0]; dy=P[1]-OtherP[1]
            distance=abs(dx)+abs(dy)
            if distance>2: continue
            elif distance<=1: return 0
            else:
                if dx!=0 and dy!=0:
                    if waitingmap[OtherP[0]+dx][OtherP[1]]=='O' or waitingmap[OtherP[0]][OtherP[1]+dy]=='O': return 0
                elif dx==0 and waitingmap[P[0]][(P[1]+OtherP[1])//2]=='O': return 0
                elif waitingmap[(P[0]+OtherP[0])//2][P[1]]=='O': return 0
    return 1

if __name__=="__main__":
    places=[
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
    print(solution(places))
