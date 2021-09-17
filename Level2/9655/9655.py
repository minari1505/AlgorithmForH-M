#9655 돌 게임 Silver 5
if int(input()) %2 ==1:
    print('SK')
else:
    print('CY')
#다른사람 해결법
print(['CY','SK'][int(input())%2])
