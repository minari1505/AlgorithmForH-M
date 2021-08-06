# 수 정렬하기2

```python
N = int(input())
_str = []

for _ in range(N):
    _str.append(int(input()))

for i in sorted(_str):
    print(i)
```

### 성공

```python
N = int(input())
_str = []

for _ in range(N):
    _str.append(input())

_str.sort()

for i in range(N):
    print(_str[i])
   
```

### 틀렸습니다

