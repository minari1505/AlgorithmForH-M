while True:
    word = input()
    pali = word[::-1]
    if word =='0':
        break
    if word == pali:
        print('yes')
    else:
        print('no')