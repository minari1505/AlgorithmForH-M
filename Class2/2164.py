from sys import stdin
n = int(stdin.readline())
card = []
for i in range(1,n+1):
    card.append(i)
while (not(len(card)== 1)):
    del card[0]
    tmp = card[0]
    del card[0]
    card.append(tmp)
print(card)