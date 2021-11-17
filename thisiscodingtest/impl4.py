while True:
    # 지도 크기
    n, m = map(int, input().split())

    # 방문 체크
    d = [[0] * m for _ in range(n)]

    # 시작 좌표 및 방향
    x, y, direction = map(int, input().split())

    # 시작 위치 방문
    d[x][y] = 1

    # 전체 맵
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 북, 동, 남, 서 위치 이동을 위한 배열
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 왼쪽 회전 함
    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    # 시뮬레이션 Start

    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x+dx[direction]
        ny = y+dy[direction]

        # 정면에 갈 곳 존재하면 이동
        if array[nx][ny] == 0 and d[nx][ny] == 0:
            d[nx][ny] = 1
            x, y = nx, ny
            count += 1
            turn_time = 0
            continue
        # 회전 후 정면에 갈 곳이 없는 경우
        else:
            turn_time += 1

        # 사방이 갈 곳 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면
            if array[nx][ny] == 0:
                x, y = nx, ny
                turn_time = 0
            # 뒤로 못가면
            else:
                break

    print(count)
