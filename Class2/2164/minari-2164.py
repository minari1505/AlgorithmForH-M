# 카드 2

```python
#1. N장의 카드
#2. lst[0] 지우고 lst[0](새로운)를 맨뒤로 보내기
#3. if len(lst) == 1 : print(lst[0])
import sys
N = int(input())
n_lst = [i for i in range(1,N+1)]
while len(n_lst) > 1:
    n_lst.pop(0) #[2,3,4,5]
    n_lst.append(n_lst[0])
    n_lst.pop(0) #[3,4,5,2]

print(n_lst[0])
```

##### 시간초과

```python
#1. N장의 카드
# N = 1 : 1
# N = 2 : 2
# N = 3 : 2
# N = 4 : 4
# N = 5 : 2
# N = 6 : 4
# N = 7 : 6
# N = 8 : 8
 

N = int(input())
num = 2
while True:
    if N <= 2:
        print(N)
        break
    num *= 2
    if num >= N:
        print((N-(num//2))*2)
        break


```

