# 30

# 만난 숫자들의 위치를 변경해서 30의 배수 만들기
# 안된다면 -1 출력

# 30의 배수 -> 일의 자리 == 0

N = list(input())
sum = 0
N.sort(reverse=True)

# 리스트 안의 숫자들을 int로 더하기 => sum에 저장
for i in N:
    sum += int(i)

if '0' not in N or sum%3 != 0:
    print(-1)
else:
    print("".join(N))

