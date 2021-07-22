# 부녀회장이 될테야

```python
### 재귀함수

#a층 b호에 살려면 (a-1)층의 +1~b호 사람들의 수만큼 들어와야함
#k층의 n호에 몇 명이 사는가
#0층,1호부터 존재
#재귀함수?

#재귀함수 만들기
def count_people(k,n):
    count = 0
    if k == 0:
        return n
    else:
        for i in range(1,n+1):
            count += count_people(k-1,i)
    return count

#T = test case의 수
T = int(input()) 
for i in range(T):
    k = int(input())
    n = int(input())
    print(count_people(k,n))

```

```python
### 2차원배열


#a층 b호에 살려면 (a-1)층의 +1~b호 사람들의 수만큼 들어와야함
#k층의 n호에 몇 명이 사는가
#전 호수에 사는 사람 + 윗층에 사는 사람 = 지금 호수에 살아야하는 사람 수 -> 2차원배열?
n_list = [[0 for i in range(14)] for j in range(15)] #아파트 2차원배열 만들기
#아파트 2차원배열 채우기
#0층 n호
for n in range(15):
    n_list[0][n-1] = n
#k층 1호 = 1명
for k in range(14):
    n_list[k][0] = 1
#k층 n호 = k-1층 n호 + k층 n-1호
for k in range(1,15):
    for n in range(1,14):
        n_list[k][n] = n_list[k][n-1] + n_list[k-1][n]       

T = int(input())
#k층 n호에 몇명있는지
for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    print(n_list[k][n-1])
```

