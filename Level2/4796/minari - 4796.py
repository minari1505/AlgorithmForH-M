# 캠핑

# 연속 P일 중 L일동안만 캠핑가능, 강산이 휴가 : V일

# 예시1 : 8일 중 5일동안 캠핑가능, 휴가 20일 => 5+5+4 => 14일
# 에시2 : 8일 중 5일동안 캠핑가능, 휴가 17일 => 5+5+4 => 11일

# 20//8==2, 20%8==4 => if 20%8 > 5 : (20//8) * 5 + 5. else: (20//8) * 5 + (20%8)
# 0 0 0 : 끝

n = 1
while True:
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V==0:
        break

    if V%P > L:
        print(f"Case {n}: {(V//P)*L + L}")
    else:
        print(f"Case {n}: {(V//P)*L + (V%P)}")
    n += 1

    