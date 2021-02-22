def solution(word):
    cnt, last = 1, ""
    list_aux = []
    ans = 0
    for i, c in enumerate(word):
        print(i,c)
        if last == c:
            cnt += 1
        else:
            if i != 0:
                list_aux.append(str(cnt))
            list_aux.append(c)
            cnt = 1
            last = c
    list_aux.append(str(cnt))
    print(list_aux)
    print("".join(list_aux))



solution("aacbbadbf")