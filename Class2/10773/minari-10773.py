# 제로

```python
# 0 입력되면 바로 전 수 지우기-> pop()
#1. 입력 : K 주어짐
#2. 정수 1개씩 주어짐
#3. 0일 경우 가장 최근의 수 지우기 / 아닐경우 숫자 추가
#4. 출력 : 최종 수의 합 

import sys
K = int(sys.stdin.readline())
lst = []
for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))
```

