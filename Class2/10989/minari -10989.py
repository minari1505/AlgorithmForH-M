#1. N개의 수 입력
#2. 오름차순 출력
#3. 아마 시간이 관건일듯..
#진짜 자증난다 잇쉬

import sys

N= int(sys.stdin.readline())
_str = [0]*10001

for i in range(N):
    _str[int(sys.stdin.readline())] += 1

for i in range(10001):
    if _str[i] != 0:
        for j in range(_str[i]):
            print(i)
