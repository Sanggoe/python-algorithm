def solution(s):
    p = 0
    y = 0
    for i in s.lower():
        if i is 'p':
            p += 1
        elif i is 'y':
            y += 1

    return True if p == y else False

