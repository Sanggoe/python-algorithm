n, m = map(int, input().split())
result = 0
nums = []

for i in range(0, n):
    nums.append(min(map(int, input().split())))

print(max(nums))
