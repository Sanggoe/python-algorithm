'''
리스트와 내장함수(2)
'''

a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=" ")
print()

for i in a:
    if not i%2:
        print(i, end=" ")
print()

for i in enumerate(a):
        print(i)
print()

b = (1, 2, 3, 4, 5)
print(b[0])

for i in enumerate(a):
        print(i[0], i[1])
print()

for index, value in enumerate(a):
        print(index, value)
print()

if all(50>x for x in a):
    print("Yes")
else:
    print("No")

if any(10>x for x in a):
    print("Yes")
else:
    print("No")
