n = int(input())
print(n*(n+1)//2)

sum = 0
for i in range(n+1):
  sum += i
print(sum)