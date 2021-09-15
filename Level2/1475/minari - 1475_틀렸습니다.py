room_num = input()
number = [0 for i in range(10)] # 사용한 플라스틱숫자 개수 저장할 리스트
for i in range(len(room_num)): #room_num 리스트 안에 있는 인덱스 돌기
    if i in [6,9]:
        if number[6] < number[9]:
            number[6] += 1
        else:
            number[9] += 1
    else:
        number[i] += 1
print(max(number))