'''
소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.
'''

# 내가 짠 코드
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
cnt = 0


def isPrime(num):
    for i in range(2, num):
        if not num%i:
            return False
    return True


for i in range(2, N+1):
    if isPrime(i):
        cnt+=1

print(cnt)


# 강의 중 강사님 코드
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
ch=[0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)


# 강의 후 다시 짠 코드
import sys
sys.stdin = open("input.txt", "r")
N = int(input())
che = [False] * (N+1)
cnt = 0

for i in range(2, N+1):
    if not che[i]:
        cnt+=1
        for j in range(i, N+1, i):
            che[j] = True
print(cnt)