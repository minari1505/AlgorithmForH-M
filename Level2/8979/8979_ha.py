#올림픽
n,k = map(int,input().split())
nation = [list(map(int,input().split())) for i in range(n)]
# lambda x : -x 내림차순 정렬, -x[1],-x[2],-x[3] 각 KEY 순서대로 정렬
nation.sort(key=lambda x: (-x[1],-x[2],-x[3]))

#Finding nation's index of k
for i in range(n):
    if nation[i][0] == k:
        index = i
#Find ranking    
for j in range(n):
    if nation[index][1:] == nation[j][1:]:
        print(j+1)
        break
