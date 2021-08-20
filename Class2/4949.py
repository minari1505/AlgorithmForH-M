while True:
    line = input()
    if line == ".":
        break
    cha = []
    answer = True

    for a in line:
        if a =="(" or a =="[":
            cha.append(a)
        elif a ==")":
            if len(cha)==0:
                answer = False
                break
            if cha[-1] =="(":
                cha.pop()
            else:
                answer = False
                break
        elif a =="]":
            if len(cha)==0:
                answer = False
                break
            if cha[-1] == "[":
                cha.pop()
            else:
                answer = False
                break

    if answer and not cha:
        print("yes")
    else:
        print("no")