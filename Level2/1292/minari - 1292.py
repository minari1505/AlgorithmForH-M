#쉽게 푸는 문제

# 1/22/333/4444/....
# 수열의 A번째 숫자부터 B번째 숫자까지의 합 구하기

A,B = map(int,input().split())

seque = []
for i in range(1,46):
    seque += [i] * i

print(sum(seque[A-1:B]))
