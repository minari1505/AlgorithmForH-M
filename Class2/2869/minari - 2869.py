# 달팽이는 올라가고 싶다

```python
#+A-B >= V 면 멈춤
# days에 며칠이 걸리는지 넣고, 출력
# i_sums = +A-B
A,B,V = map(int,input().split())
i_sums = 0
days = 0
while i_sums < V:
    days += 1
    i_sums += A
    if i_sums == V:
        break
    i_sums -= B
    
print(days)
```

```python
#+A-B >= V 면 멈춤
# 반복문이 느려서 시간초과난다면, 공식세워야하니
A,B,V = map(int,input().split())
days = (V-B)/(A-B)
print(int(days) if days == int(days) else int(days)+1)
```

