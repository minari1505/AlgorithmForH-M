```python
x,y,w,h = map(int,input().split())
dist = []
dist.append(x-0)
dist.append(abs(x-w))
dist.append(y-0)
dist.append(abs(y-h))
print(min(dist))

#1. 현재 서있는 위치인 x가 0과 w 중 어느곳에 더 가까운지(y 고정), y가 0과 h중 어느 곳에 더 가까운지(x 고정) 판단 => 값들 리스트에 저장
#2. 저장한 리스트 중 min값 출력

```

