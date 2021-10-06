# 올림픽

# 국가의 수, 등수를 알고싶은 국가
# 국가숫자, 금, 은, 동 

# num,gold,silver,bronze 를 리스트에 저장, 2차원배열 만들기
# 자신보다 잘한 나라 수 + 1 => 숫자를 하나씩 올려가면 되지않나

import sys
N,K = map(int,sys.stdin.readline().split()) #N : 국가의 수, K : 등수를 알고싶은 국가
medal = [list(map(int,input().split())) for _ in range(N)] #num,gold,silver,bronze 저장한 2차원배열
medal.sort(key = lambda x : (x[1],x[2],x[3]), reverse=True) #금은동 기준으로 정렬, 내림차순

for i in range(N):
    if medal[i][0] == K:
        count = i
        
for i in range(N):
    if medal[count][1:] == medal[i][1:]:
        print(i+1)
        break





    
