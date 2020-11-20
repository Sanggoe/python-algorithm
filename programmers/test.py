import math


# 무식하게 짜는 방법 1
import math


def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, int(math.sqrt(n + 1)) + 1):
        if i in num:
            num -= set(range(i * 2, n + 1, i))  # 배수 모두 삭제

    return len(num)


print(solution(10))
