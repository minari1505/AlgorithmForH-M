import sys
from collections import deque
N = int(sys.stdin.readline())
for _ in range(N):
    N, M =map(int,sys.stdin.realine())
    K = deque(map(int,sys.stdin.readline().split()))
    max= max(K)
    i=0
    count=0
    while N:
        
        if K[i] == max:
            K.popleft()
            count +=1
            
        K.append(K[i].popleft())

