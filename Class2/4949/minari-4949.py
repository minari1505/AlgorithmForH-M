# 균형잡힌세상

```python
while True:
    a = input()
    if a == ".":
        break
    stack = []
    answer = True
    
    for j in a:
        if j == "(" or j == "[":
            stack.append(j)
        
        elif j == ")":
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                answer = False
                break
                
        elif j == "]":
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                answer = False
                break

    if answer and not stack:
        print("yes")
    else:
        print("no")
```

