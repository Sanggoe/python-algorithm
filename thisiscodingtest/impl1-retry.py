n = int(input())
x, y = 1, 1
plans = input().split(' ')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direct = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(direct)):
        if plan == direct[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if not (1 <= nx <= n and 1 <= ny <= n ):
        continue

    x, y = nx, ny

print(x, y)
