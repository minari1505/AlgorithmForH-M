# 다리 놓기

# 사이트 = 다리짓기 가능한 곳 (한 사이트에는 한 개의 연결만 가능)
#1. T = 테스트 케이스 갯수
#2. N,M = 강의 서,동에 있는 사이트 갯수
#3. 조합?

# 조합 구현하기

# 동쪽 수 5*4*..(5-i) / i*(i-1)*(i-2)...*(2)

T = int(input())
for i in range(T):
    denom = 1
    numer = 1
    N, M = map(int,input().split()) # N = 서쪽 사이트 갯수, M = 동쪽 사이트 갯수
    for j in range(N):
        numer *= (M-j) #분자
        denom *= (j+1) #분모
    print(int(numer/denom))

# 두번째 for문을 한 번 돌고 numer과 denom을 초기화하지 않으면 씌여진 값에 또 *가 되어서 값이 안맞는다 8ㅅ8
