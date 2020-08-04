'''
함수 만들기

def add(a, b):
    c = a+b
    print(c)

add(3, 2)
add(5, 7)

def add(a, b):
    c = a+b
    return c

x=add(3,2)
print(x)

def add(a, b):
    c = a+b
    d = a-b
    return c, d

print(add(3,2), end=" ") 
'''

def isPrime(n):
    for i in range(2, n):
        if not n%i:
            return False
    return True

a=[12, 13, 7, 9, 19]

for n in a:
    if isPrime(n):
        print(n, end=" ")
