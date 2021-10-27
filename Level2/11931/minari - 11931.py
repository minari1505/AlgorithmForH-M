# 수 정렬하기 4

# N개의 수 주어짐, 내림차순으로 정렬

import sys
lst = []
N = int(sys.stdin.readline())

for _ in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)

for i in lst:
    print(i)
