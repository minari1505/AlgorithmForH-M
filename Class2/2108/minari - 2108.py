# 통계학

```python
#1. N개의 값 리스트에 입력받기
#2. 산술평균, 중앙값, 최빈값, 범위 구하기
#3. 출력

N = int(input())  # N은 홀수
lst = [int(input()) for i in range(N)]

arithmetic_mean = sum(lst) / N #산술평균
median = 0 #중앙값
mode = 0 #최빈값
difference = max(lst) - min(lst) #범위

#중앙값 구하기
lst.sort()
median = lst[int(N/2)]

#최빈값 구하기
    #1. 0*max(lst)개로 채워진 리스트 생성
    #2. lst의 요소가 3이라면 2번 인덱스에 +1
    #3. mode_lst 중 최댓값 인덱스 번호 +1
mode_lst = [0 for i in range(max(lst))]
for i in lst:
    mode_lst[i-1] += 1
mode = mode_lst.index(max(mode_lst))+1
print(mode)

```

#### 최빈값 구하다가 패스.. 다른곳에서는 다 돌아가는데 lst값이 모두 -일땐 안되더라궁

```python
#1. N개의 값 리스트에 입력받기
#2. 산술평균, 중앙값, 최빈값, 범위 구하기
#3. 출력
import sys
N = int(input())  # N은 홀수
lst = [int(sys.stdin.readline()) for i in range(N)]

arithmetic_mean = sum(lst) / N #산술평균
median = 0 #중앙값
difference = max(lst) - min(lst) #범위

#중앙값 구하기
lst.sort()
median = lst[int(N/2)]

#최빈값 구하기
def mode(lst):
    import collections
    tmp = collections.Counter(lst).most_common()

    if len(tmp) > 1:
        if tmp[0][1] == tmp[1][1]:
            return tmp[1][0]
        else:
            return tmp[0][0]
    else:
        return tmp[0][0]

print(int(round(arithmetic_mean,0)))
print(median)
print(mode(lst))
print(difference)


```

