while(1) :
    y, x = input()
    x = int(x)
    y = ord(y) - ord('a') +1

    steps = [(-2,-1), (-2,1), (-1,-2), (1,-2), (-1,2), (1,2), (2,-1), (2,1)]
    count = 0

    for i, j in steps:
        if (0 < (x+i) <= 8 and 0 < (y+j) <= 8):
            count += 1

    print(count)
