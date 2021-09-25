# 1
def solution(id_list, report, k):
    cntReport={id:0 for id in id_list}
    nameReport={id: set() for id in id_list}
    
    for r in report:
        user, reportid = r.split()
        if reportid not in nameReport[user]:
            nameReport[user].add(reportid)
            cntReport[reportid]+=1
    ReportK={id for id in id_list if cntReport[id] >= k}
    answer=[len(nameReport[id].intersection(ReportK)) for id in id_list]
    
    return answer

#2
import math

def isPrime(n):
    if n==1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def solution(n, k):
    count=0
    
    b=''
    while n>0:
        n, m = divmod(n,k)
        b+=str(m)
    nums=[int(num) for num in b[::-1].split('0') if num.isdigit()]
    
    for n in nums:
        if isPrime(n): count+=1
    return count

# 3
from datetime import datetime, timedelta
from collections import defaultdict
import math
def solution(fees, records):
    car_info=defaultdict(list)
    car_totaltime=defaultdict(timedelta)
    
    for r in records:
        t, id, c = r.split(' ')
        if c=='IN': car_info[id].append(datetime.strptime(t, '%H:%M'))
        elif c=='OUT': car_totaltime[id] += datetime.strptime(t, '%H:%M')-car_info[id].pop()
    
    for id, record in car_info.items():
        if record: car_totaltime[id] += datetime.strptime('23:59', '%H:%M')-car_info[id].pop()
    
    result=[]
    for id, time in car_totaltime.items():
        extrafee=0
        if time.seconds//60 > fees[0]: extrafee=(math.ceil((time.seconds//60 - fees[0])/fees[2])*fees[3])
        result.append((id, fees[1]+extrafee))
        
    return [totalfee for id, totalfee in sorted(result, key=lambda x: x[0])]

#4
from itertools import combinations_with_replacement

def solution(n, info):
    max_score=-1; max_seq=[-1]
    for cmb in combinations_with_replacement(list(range(11)), n):
        sequence=[0]*11
        for i in cmb: sequence[10-i]+=1
            
        score=get_difference(info, sequence)
        if score > max_score: 
            max_score, max_seq = score, sequence
        elif score == max_score:
            for m, s in zip(max_seq[::-1], sequence[::-1]):
                if s>m: max_seq=sequence; break
                elif s<m: break
        
    return max_seq if max_score > -1 else [-1]


def get_difference(info, seq_of_ryan):
    apeach_score=0; ryan_score=0
    for i in range(11):
        if info[i] == seq_of_ryan[i] == 0: continue
        elif info[i] >= seq_of_ryan[i]: apeach_score+=10-i
        else: ryan_score+=10-i
    if apeach_score >= ryan_score: return -1
    else: return ryan_score - apeach_score

#6
def solution(board, skill):
    for s in skill:
        degree= -1 if s[0]==1 else 1
        for i in range(s[1], s[3]+1):
            for j in range(s[2], s[4]+1):
                board[i][j]+=s[5]*degree
    count=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>=1: count+=1

    return count

#7
from collections import deque
from collections import defaultdict
def solution(board, aloc, bloc):
    px=[1,-1,0,0]; py=[0,0,1,-1]
    tree=defaultdict(list)

    # create Tree
    stack=
    while stack:
        node=stack.pop()
        for i in range(4):
            curx, cury = x[0]+px[i], x[1]+py[i]
            if 0<=curx<=len(board) and 0<=cury<=len(board) and board[curx][cury]==1:
                stack.append([curx, cury])
                tree[''.join(node)].append([curx, cury])
    
    # traverse
    
        
    return answer
        
def is_available_to_move(x, board):
    px=[1,-1,0,0]; py=[0,0,1,-1]

    for i in range(4):
        curx, cury = x[0]+px[i], x[1]+py[i]
        if 0<=curx<=len(board) and 0<=cury<=len(board) and board[curx][cury]==1: continue
        else: return False
    return True