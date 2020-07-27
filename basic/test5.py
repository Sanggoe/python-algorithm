'''
반복문을 이용한 문제풀이
  1) 1부터 N까지 홀수 출력
  2) 1부터 N까지 합 구하기
  3) N의 약수 출력

N = int(input("숫자 입력> "))
for i in range(1, N+1):
    if i%2:
        print(i)

sum
print(type(sum))
sum=0
N = int(input("숫자 입력> "))
for i in range(1, N+1):
    sum+=i
print(sum)

N = int(input("숫자 입력> "))
for i in range(1, N+1):
    if not N%i:
        print(i, end=" ")
'''
