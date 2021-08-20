# 숫자카드 2

```python
#1. 입력 : N
#2. 입력 : 숫자카드에 적혀있는 정수
#3. 입력 : M
#4. 입력 : 몇개 가지고 있는 숫자카드인지 구해야 할 정수
from sys import stdin
from collections import Counter
N = stdin.readline()
N_lst = stdin.readline().split()
M = stdin.readline()
M_lst = stdin.readline().split()
Coun = Counter(N_lst)
print(' '.join(f'{Coun[i]}'if i in Coun else "0" for i in M_lst))
```

