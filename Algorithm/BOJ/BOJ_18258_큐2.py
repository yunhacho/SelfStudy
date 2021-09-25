from sys import stdin
from collections import deque

queue=deque()
operate={ 'push': lambda x: queue.append(x), 'pop': lambda: queue.popleft() if bool(queue) else -1, 'size': lambda: len(queue), 
            'empty': lambda: 0 if bool(queue) else 1, 'front': lambda: queue[0] if bool(queue) else -1, 'back': lambda: queue[-1] if bool(queue) else -1}

for _ in range(int(input())):
    cmd=stdin.readline().split()
    if cmd[0]=='push': operate[cmd[0]](int(cmd[1]))
    else: print(operate[cmd[0]]())