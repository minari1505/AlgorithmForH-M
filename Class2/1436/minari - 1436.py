# 영화감독 숌

```python
#666,1666,,,,10666,11666,12666,13666,14666,15666
#16660~16669
#17666,18666,19666,20666,21666,22666,23666,24666,25666
#26660~26669
#27666,28666,29666,30666,31666,32666,33666,34666,35666
#36660~36669
#66600,66601,66602,,,66699

# 6이 연속으로 3개 나온다면 a += 1
# a == N일 때 N 출력하면 안되나
# 처음 시작은 666
N = int(input())
a = 0
three_six = 666
while True:
    if '666' in str(three_six):
        a +=1
    if a == N:
        print(three_six)
        break
    three_six += 1

```
