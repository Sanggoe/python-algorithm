h, m = map(int, input().split())
r = (h*60+m-45)%1440
h = r//60
m = r%60
print(h, m)