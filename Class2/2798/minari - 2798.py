# 블랙잭

```python
#1. N장의 카드 중 3장 고름
#2. M을 넘지 않고, M과 비슷한 사람이 이김

# 3중 for문으로 N장 중 3장 고름
# 3장의 합이 M을 넘지 않으면, answer에 저장
# 새로운 answer값이 더 크다면 새로운 answer 값을 저장하기
N,M = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if lst[i]+lst[j]+lst[k] <= M:
                answer = max(answer, lst[i]+lst[j]+lst[k])
            else:
                pass
print(answer)
```

