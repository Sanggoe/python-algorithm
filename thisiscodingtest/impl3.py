y, x = (input())
y = ord(y)-ord('a')+1
x = int(x)
num = 0

# 내가 푼 if문 더미
'''
if (x>2):
    if (y>1):
        num+=1
    if (y<8):
        num+=1
if (x<6):
    if (y>1):
        num+=1
    if (y<8):
        num+=1
if (y>2):
    if (x>1): 
        num+=1
    if (x<8):
        num+=1
if (y<6):
    if (x>1):
        num+=1
    if (x<8):
        num+=1

print(num)
'''

# 반복문 풀이
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        num+=1

print(num)


# 뭐가 더 효율적일까?
