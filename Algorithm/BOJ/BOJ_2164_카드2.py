from collections import deque

def get_last_card(N: int) -> int:
    cards=deque(range(1,N+1))
    while cards: discard=cards.popleft(); cards.rotate(-1)
    return discard

if __name__=="__main__":
    N=int(input())
    print(get_last_card(N))