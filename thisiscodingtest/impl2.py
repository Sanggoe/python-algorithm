n = int(input())
t = 0

for h in range(0, n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                t+=1

print(t)
