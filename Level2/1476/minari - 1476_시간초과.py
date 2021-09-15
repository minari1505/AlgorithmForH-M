# 날짜계산

#수 세개를 이용해 연도 나타냄. (지구(E),태양(S),달(M))
#1년이 지날 때 마다 E,S,M은 한 수씩 증가, 범위가 넘어가면 다시 1

# while문 써서 n += 1 씩 올리고, n % 15 == E and n % 28 == S and n % 19 == M 이면 n 출력?

E,S,M = map(int,input().split())

n = 1
while n > 0:
    if n%15==E and n%28==S and n%19==M:
        print(n)
        break
    else:
        n += 1
        


    