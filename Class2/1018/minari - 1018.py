# 체스판 다시 칠하기

```python
#체스판 다시 칠하기
#2차원 배열?
#if a[i][j] != a[i][j+1], a[i+1][j] : pass else: answer += 1
#8*8 크기로 잘라냈을 때 최소 개수의 answer 를 제출

#1.원본 크기의 체스판 2차원 배열로 받아오기
N,M = map(int,input().split())
original = []
count = []

for _ in range(N):
    original.append(input())
    
for a in range(N-7):
    for b in range(M-7):
        ind1 = 0
        ind2 = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != "W":
                        ind1 += 1
                    if original[i][j] != "B":
                        ind2 += 1
                else:
                    if original[i][j] != "B":
                        ind1 += 1
                    if original[i][j] != "W":
                        ind2 += 1
        count.append(min(ind1, ind2))
print(min(count))
   
```

