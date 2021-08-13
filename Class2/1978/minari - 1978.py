# 소수 찾기

```python
#1. N 주어짐
#2. N개의 수 주어짐(한줄로)
#3. 소수 = 자기자신과 1로만 나누어지는 수
#   1과 자기자신 외 다른 수로 나누었을 때 나누어떨어지면 안됨
N = int(input())
prime_number = map(int,input().split())
count = 0
count_num = 0
for num in prime_number:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                count_num += 1
        if count_num == 0:
            count += 1
            count_num = 0
print(count)
```

### 틀렸습니다

##### 정답과 차이가 count_num = 0 을 전역변수로 둔 것 밖에 없는데 왜 안될까



```python
#1. N 주어짐
#2. N개의 수 주어짐(한줄로)
#3. 소수 = 자기자신과 1로만 나누어지는 수
#   1과 자기자신 외 다른 수로 나누었을 때 나누어떨어지면 안됨
import sys
N = int(input())
prime_number = list(map(int,input().split()))
count = 0
for num in prime_number:
    count_num = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                count_num += 1
        if count_num == 0:
            count += 1
            count_num = 0
print(count)
```

