# 색종이

# 첫 번째 자연수 : x 두 번째 자연수 : y -> (x,y)

# 겹치는부분 해결

N = int(input())
lst = [[0 for _ in range(101)]for _ in range(101)] # 가로 100, 세로 100인 좌표를 리스트로 표현하기

for i in range(N):
    X,Y = map(int,input().split())
    # 가로,세로 10인 정사각형 색종이이므로 X축~X축+10, Y축~Y축+10 까지 1로 채워짐 표시
    for i in range(X,X+10):
        for j in range(Y,Y+10):
            lst[i][j] = 1
        
sum = 0
for i in lst:
    sum += i.count(1)
print(sum)