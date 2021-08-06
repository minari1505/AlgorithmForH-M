# 나이순 정렬

```python
#1. N만큼 나이 이름 주어짐
#2. 2차원배열? 로 나이만 비교, sort
#3. if 나이가 == , i가 빠른 순으로 정렬

#1.
N = int(input())
lst = []
#2.
for i in range(N):
    age,name = map(str,input().split())
    lst.append([age,name])
lst.sort(key = lambda x:x[0])
#위의 sort까지만 해도, 나이가 같다면 i 가 빠른순으로 정렬됨 => 따로 정렬필요x

for i in range(N):
    print(int(lst[i][0]),end=' ')
    print(lst[i][1])
```

#### 오답

```python
#1. N만큼 나이 이름 주어짐
#2. 2차원배열? 로 나이만 비교, sort
#3. if 나이가 == , i가 빠른 순으로 정렬
#4. 출력

#1.
N = int(input())
lst = []
#2.
for _ in range(N):
    age,name = map(str,input().split())
    lst.append([age,name])
lst.sort(key = lambda x:int(x[0]))
#위의 sort까지만 해도, 나이가 같다면 i 가 빠른순으로 정렬됨 => 따로 정렬필요x

#4. 출력
for member in lst:
    print(member[0],member[1])
```

#### 성공

##### .sort를 x[0]으로 하면 str기준 sort가 되므로 9보다 10,11..이 빨리나올것같음..

