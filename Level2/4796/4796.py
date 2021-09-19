#4796 캠핑 Silver 5
i=0
while 1:
    l,p,v = map(int,input().split())
    if l+p+v == 0:
        break
    i+=1
    print('Case {0}: {1}'.format(i,(v//p)*l +  min((v %p),l)))
