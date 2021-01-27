# 내가 짠 코드
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
N, K = map(int, input().split())
nums = list(map(int, input().split()))
results = set()
for i in combinations(nums, 3):
    results.add(sum(i))

print(sorted(results, reverse=True)[K-1])