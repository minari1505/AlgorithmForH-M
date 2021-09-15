#막대기
#64cm 막대 하나
#절반씩 자른 크기를 가지고 X 만들기
# 64, 32, 16, 8, 4, 2, 1


X = int(input())
stick = [64,32,16,8,4,2,1] #stick이 가질 수 있는 크기 리스트에 저장
count = 0

for i in range(len(stick)):
    # 만약 X가 stick[i]보다 크거나 같으면, X에서 stick[i]를 빼고 count에 1 추가
    if X >= stick[i]:
        X -= stick[i]
        count += 1
        
    elif X == 0:
        break

print(count)