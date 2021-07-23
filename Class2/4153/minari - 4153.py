```python
#직각삼각형

#여러 개의 테스트케이스 -> 테스트케이스 개수 모르므로 While문 이용
#1.a,b,c =list(map(int,input().split()))
#2.sort()로 오름차순 정렬시키기

while True:
    side = []
    a,b,c = map(int,input().split())
    side += a,b,c
    side.sort()  #2.
    if a==0 and b==0 and c==0:
        break
    
    if side[0]**2 + side[1]**2 == side[2]**2:
        print("right")
    else:
        print("wrong")
```

