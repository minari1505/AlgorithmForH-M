# 괄호

```python
a = int(input())
for i in range(a):
    b = input()
    lst = list(b)
    sum = 0

    for i in lst:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0 :
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    
    elif sum == 0:
        print("Yes")
```

### 틀렸습니다

```python
a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
```

### 맞았습니다 왜?

