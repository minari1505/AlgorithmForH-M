# 분해합

```python
# 분해합 : 생성자+N의 각 자리수
# 256 = 245 + 2 + 4 + 5
# 입력: 분해합, 출력 : 생성자
N = int(input())
answer = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            prod = i*100 + j*10 + k
            if prod + i + j + k == N:
                answer.append(prod)

if answer != 0:
    print(min(answer))
else:
    print(0)
```

#### 런타임 에러 (ValueError)



```python
# 분해합 : 생성자+N의 각 자리수
# 256 = 245 + 2 + 4 + 5
# 입력: 분해합, 출력 : 생성자
N = int(input())
count = 0
for i in range(1,N+1):
    st_i = list(map(int,str(i)))
    decomp = i + sum(st_i)
    if decomp == N:
        count = i
        break
print(count)
```

#### 브루트포스

