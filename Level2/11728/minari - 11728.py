#배열 합치기

# A배열 + B배열, 오름차순으로 정렬하기

# 1. A 배열의 크기 N, B 배열의 크기 M
# 2. A 배열의 내용
# 3. B 배열의 내용

import sys
A,B = map(int,sys.stdin.readline().split())
lst_A = list(map(int,sys.stdin.readline().split()))
lst_B = list(map(int,sys.stdin.readline().split()))

lst_C = []

lst_C.extend(lst_A)
lst_C.extend(lst_B)
lst_C.sort()

for i in range(len(lst_C)):
    print(lst_C[i], end = ' ')