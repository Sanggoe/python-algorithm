# 내가 짠 코드
import sys

sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
nums = sorted([i + j for i in range(1, N+1) for j in range(1, M+1)])
max = 0
res = list()
for n in set(nums):
    count = nums.count(n)
    if max < count:
        res = [n]
        max = count
    elif max == count:
        res.append(n)

for n in sorted(res):
    print(n, end=" ")
