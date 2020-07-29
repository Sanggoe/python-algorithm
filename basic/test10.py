'''
2차원 리스트 생성과 접근
'''

a=[2]*10
b=[1]*10
print(a)

a=[[0]*3 for _ in range(3)]
print(a)
a[0][1]=1
print(a)
a[1][1]=2
print(a)

for x in a:
    for y in x:
        print(y, end=" ")
    print()
print()
print()
print()

a=[[2]*2 for _ in range(3)]
b=[[1]*2 for _ in range(3)]
c=[[]]
print(len(a), len(a[0]))
print(a)
print(b)
print(c)
print()

for i in range(len(a)):
    print(i)
