#중복 빼고 정렬하기

# N개의 정수를 오름차순으로 정렬, 같은 정수는 한 번만 출력 -> set

N = int(input())
num = list(map(int,input().split()))
num = list(set(num))
num.sort()

for i in range(len(num)):
    print(num[i],end= ' ')
