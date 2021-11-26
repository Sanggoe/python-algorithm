n = int(input())
x, y = 1, 1
plan = input().split(" ")

for c in plan:
    if c == 'L':
        if y > 1:
            y-=1
    elif c == 'R':
        if y < n:
            y+=1
    elif c == 'U':
        if x > 1:
            x-=1
    else:
        if x < n:
            x+=1

print(x, y)
