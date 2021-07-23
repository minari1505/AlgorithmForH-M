```python
#호 수 1번부터 6층이 채워지면 그 다음 호 수 2번으로 넘어감.
#층 수는 아래부터 차례대로 채워짐
#1. input : T
#2. input : H(층 수) , W(호 수), N(몇 번째 손님)
#3. print : 배정되는 방 번호

# 층 수 * 100 + 호 수 == 배정되는 방

T = int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    floors = N%H
    units = (N//H)+1
    if floors == 0:
        floors = H
    if floors == H:
        units = N//H
    print(floors*100 + units)
```

