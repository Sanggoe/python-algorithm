'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())
print(msg.lower())
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end=" ")
print()

for i in msg:
    print(i, end=" ")
print()

for i in msg:
    if i.isupper():
        print(i, end=' ')
print()

for i in msg:
    if i.islower():
        print(i, end=' ')
print()

for i in msg:
    if i.isalpha():
        print(i, end=' ')
print()

tmp='AZaz09'
for i in tmp:
    print(ord(i))
print(type(tmp))

tmp=65
print(chr(tmp))
print(type(tmp))
