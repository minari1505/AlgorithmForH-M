# 벌집

```python
#지나가는 방의 개수 1개:1   =>1
#지나가는 방의 개수 2개:2~7 =>6
#지나가는 방의 개수 3개:8~19 =>12
#지나가는 방의 개수 4개:20~37 =>18
#지나가는 방의 개수 5개:38~61 =>24
#방의 개수 = 6(n-1)씩 증가하는 계차수열
N = int(input())
room_num = 1 #같은 방의 개수를 가진 방의 수
room_count = 1 #지나가는 방의 개수
while N > room_num:
    room_num += 6*room_count
    room_count += 1
print(room_count)
```

