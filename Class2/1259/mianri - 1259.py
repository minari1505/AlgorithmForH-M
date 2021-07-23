# 팰린드롬수

```python
#앞뒤가 똑같은 수 = 팰린드롬수
#1. while True: , 0 주어지면 break
#2. for문, T[i] == T[-i] 라면 yes, 아니면 no
while True:
    T = str(input())
    if T == "0":
        break
    if T[::-1] == T:
        print('yes')
    else:
        print('no')
        
```

