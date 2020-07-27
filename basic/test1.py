'''
변수 형식은 다른 언어랑 비슷하다.
주석은 # 또는 이렇게 작은 따옴표 세 개 연속하면 여러줄 주석
'''

a=1
A=2
A1=3
_b=4
print(a, A, A1, _b)
a, b, c = 3,2,1
print (a,b,c)

# 값 교환
a, b = b, a
print(a,b)

# 변수 타입
a=123456789
print(a)
a=12,123456789123456789
print(a)
a="studnet"


# 출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number",a,b,c)
print(a,b,c,sep=', ')
print(a,b,c,sep='')
print(a,b,c,sep='\n')
