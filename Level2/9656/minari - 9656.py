# 돌 게임2

# 돌 N개 존재. 상근-창영-상근... . 돌은 1개 or 3개. 마지막 돌 가져가면 lose
# 상근이 이기면 SK, 창영이 이기면 CY 출력

#N = 3, 1-1-1 = CY, 3 = CY
#N = 5, 1-1-1-1-1 = CY, 3-1-1 = CY
#N = 4, 1-1-1-1 = SK, 3-1 = SK
#N = 8, 1-1-1-1-1-1-1-1 = SK, 3-3-1-1 = SK
#N이 홀수이면 CY 승, 짝수이면 SK 승

N = int(input())

if N%2 == 0:
    print("SK")
else:
    print("CY")