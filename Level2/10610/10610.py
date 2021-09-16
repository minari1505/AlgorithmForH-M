n = list(input())
'''
while n % 30 != 0:
    s = list(str(n))
    random.shuffle(s)
    print(s)
    n = int(''.join(s))
'''
n.sort(reverse=True)
sum =0
for i in n:
    sum += int(i)
if sum %3 !=0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))    