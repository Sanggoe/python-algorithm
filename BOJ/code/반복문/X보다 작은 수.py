import sys
N, X = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
for n in nums:
  if n < X:
    print(n, end=" ")