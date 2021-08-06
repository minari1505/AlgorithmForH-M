# 수 정렬하기3

```python
#1. N개의 수 입력
#2. 오름차순 출력
#3. 아마 시간이 관건일듯..
#진짜 자증난다 잇쉬

import sys

N= int(sys.stdin.readline())
_str = [0]*10001

# if 숫자가 5라면 _str[5]에 1을 추가
for i in range(N):
    _str[int(sys.stdin.readline())] += 1

#0부터 10000까지 for문 돌리기
#_str[i]에 숫자가 들어가있다면, 들어가있는 숫자만큼 i를 출력
for i in range(10001):
    if _str[i] != 0:
        for j in range(_str[i]):
            print(i)
```



