h, m = map(int, input().split())
t = int(input())
r = (h*60+m+t)%1440
h = r//60
m = r%60
print(h, m)