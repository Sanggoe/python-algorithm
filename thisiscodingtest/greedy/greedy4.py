s = int(input())
i = 0
while s > 0:
    i += 1
    s -= i

if i == 1:
    print(1)
elif s == 0:
    print(i)
else:
    print(i-1)
