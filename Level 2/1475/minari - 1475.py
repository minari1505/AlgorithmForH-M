#방 번호

#한 세트 : 0~9, 6=9,9=6

#1. room_num = list(int,input().split())
#2. number = [0 for i in range(10)] -> [0,0,...,0]
#3. room_num이 6,9일 때 : 인덱스 6,9 중 작은 인덱스의 숫자를 올리기
#4. else: number[room_num[i]] += 1
#5. print(min(number))

room_num = input()
number = [0 for i in range(10)] # 사용한 플라스틱숫자 개수 저장할 리스트
for i in range(len(room_num)): #room_num 리스트 안에 있는 인덱스 돌기
    num = int(room_num[i])
    if num in [6,9]:
        if number[6] < number[9]:
            number[6] += 1
        else:
            number[9] += 1
    else:
        number[num] += 1
print(max(number))
