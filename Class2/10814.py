n = int(input())
li = []
for i in range(n):
    li.append(list( input().split()))
li.sort(key=lambda x:int(x[0]))
for j in range(n):
    print(li[j][0], li[j][1])

print("--------------------")
for k in li:
    print(k)