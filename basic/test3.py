'''
조건문 if(분기, 중첩)

x=7
if x==7:
    print("Lucky")
if x!=5:
    print("test")

# 중첩
x=15
if x>=10:
    if x%2:
        print("10이상의 홀수")
    else :
        print("10이상의 짝수")

x=15
if x>0:
    if x<10:
        print("10보다 작은 자연수")
    else :
        print("10이상의 자연수")

x=15
if x>0 and x<10:
    print("10보다 작은 자연수")
else :
    print("10이상의 자연수")

x=15
if 0<x<10:
    print("10보다 작은 자연수")
else :
    print("10이상의 자연수")

'''

x=50
if x>=90:
    print('A')
elif x>80:
    print('B')
elif x>70:
    print('C')
elif x>60:
    print('D')
else :
    print('F')
