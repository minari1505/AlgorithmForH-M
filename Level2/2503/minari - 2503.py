# 숫자 야구
import sys
from itertools import permutations

num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#순열로 숫자 세개씩 뽑기
num = list(permutations(num_lst, 3))
N = int(sys.stdin.readline())

for _ in range(N):
    test, s, b = map(int,sys.stdin.readline().split())
    test = list(str(test))
    remove = 0 # 배열에서 제거된 갯수

    length = len(num)
    # 순열로 세개씩 뽑힌 갯수만큼 for문 돌기
    for i in range(length):
        count_s = count_b = 0
        i -= remove

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    count_s += 1
                else:
                    count_b += 1
        
        if count_s != s or count_b != b:
            num.remove(num[i])
            remove += 1

print(len(num))
