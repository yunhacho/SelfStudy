
def hanoi(N, From=1, To=3, Sub=2):
    if N==1: print(From, To)
    else:
        hanoi(N-1, From, Sub, To)
        print(From, To)
        hanoi(N-1, Sub, To, From)
    return

hanoi(7)
