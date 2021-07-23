A, B ,V= map(int,input().split())
day =0 
while True:
    V = V - A 
    day +=1
    if V <= 0:
        break
    V += B
print(day)

