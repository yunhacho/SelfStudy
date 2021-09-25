from sys import stdin

if __name__=="__main__":
    N, C = map(int, stdin.readline().split())
    *pos=map(int, stdin.readlines())
    print(N,C,pos)