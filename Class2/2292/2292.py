n = int(input())
c=1
room=1
while 1:
    if(n>room):
        room+=c*6
        c+=1
    else:
        break
print(c)
