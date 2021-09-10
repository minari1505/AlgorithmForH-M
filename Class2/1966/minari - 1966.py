# 프린터 큐

```python
from collections import deque 
t = int(input()) 
for _ in range(t):
    n , x = map(int,input().split())
    que = deque(list(map(int,input().split())))
    index_que = deque(list(range(n)))
    cnt = 0 
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if index_que.popleft() == x:
                print(cnt)
        else:
            que.append(que.popleft())
            index_que.append(index_que.popleft())
```

