n = a = int(input())
c = 0

while True:
  n = n%10*10 + (n//10 + n%10)%10
  print(n, c)
  c += 1
  if a == n:
    print(c)
    break