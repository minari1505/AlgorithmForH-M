# 덩치

```python
#키,몸무게 둘 다 더 커야 등수가 올라감
#만약 둘 중에서 비교가 안된다면 같은 등수

#1. 2차원 배열로 몸무게(x),키(y) 받기
#2. 모든 사람의 등수를 1로 놓고, 전사람의 몸무게<다음사람의 몸무게 and 전사람의 키<다음사람의 키 일 때에만 +1
#2-1 이중for문 써서 돌리면 되지않나?

N = int(input())
people = []

for i in range(N):
    weight,height = map(int,input().split())
    people.append([weight,height])

# 현재 사람의 기준으로 rank를 매기기 때문에 이전 사람보다 모두 작을때에만 rank +=1
for j in people:
    rank = 1
    for k in people:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank)
```

