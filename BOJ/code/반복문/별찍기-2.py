import sys
n = int(sys.stdin.readline())
s = '*'
b = ' '
for i in range(0, n):
  print(b*(n-(i+1)) + s*(i+1))