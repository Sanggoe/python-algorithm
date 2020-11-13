# 무식하게 짜는 방법 1
def solution(n, m):
    min, max = sorted([n, m])
    while 1:
        remain = max % min
        if not remain:
            return [min, n*m//min]
        max, min = min, remain


print(solution(5, 2))
