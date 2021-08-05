import sys
from collections import deque
n = int(sys.stdin.readline())
card = deque([i for i in range(1,n+1)])
while (not(len(card) == 1)):
    card.popleft()
    back = card.popleft()
    card.append(back)
print(card[0])