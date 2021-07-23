# 설탕배달

```python
# 설탕배달
# 5와 3을 최소한의 개수로 이용해 N을 만들어야함
# 만약 N%5==0 이라면 count == N//5
# N%5 != 0 이라면 N-3을 하고 count +=1
# N=0일때까지 반복
N = int(input())
count = 0
while N>=0:
    if N%5 == 0:
        count += N//5
        print(count)  
        break
    else:
        N -= 3
        count += 1  
else:
    print('-1')
    
```

