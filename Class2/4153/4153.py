while 1:
    tri = list(map(int,input().split()))
    if( tri[0] == 0 and tri[1]==0 and tri[2]==0):
        break
    for i in range(1,3):
        if tri[0] < tri[i]:
            tmp = tri[0]
            tri[0] = tri[i]
            tri[i]=tmp
    if (tri[0]**2 == tri[1]**2 + tri[2]**2):
        print("right")
    else:
        print("wrong")
