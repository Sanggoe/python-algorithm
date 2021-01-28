# 내가 짠 코드
import sys

sys.stdin = open("input.txt", "r")
N = int(input())
nums = list(map(int, input().split()))
avg = int(sum(nums) / len(nums) + 0.5)
min = 1

for i, v in enumerate(nums):
    if abs(avg - v) < abs(avg - nums[min]):
        min = i
    elif abs(avg - v) == abs(avg - nums[min]):
        if v > nums[min]:
            min = i

print(avg, min+1)
