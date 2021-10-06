# 뒤집기

# S = 0과 1로 이뤄진 문자열
# 모두 0 or 1로 뒤집히면 끝

# 0or1이 끊기는 부분을 저장(0->1 : 0, 1->0 : 1로 저장). 마지막 요소까지 저장.횟수가 더 적은 쪽을 출력
# 0001100 -> 0,1,0 -> 1이 하나이므로 1 출력
# 110010101011 -> 1,0,1,0,1,0,1,0,1 -> 4

import sys
S = list(str(input()))
count_num = []

for i in range(1,len(S)):
    if S[i-1] != S[i]:
        count_num.append(S[i-1])
    else:
        pass

count_num.append(S[-1])

print(min(count_num.count('0'),count_num.count('1')))
