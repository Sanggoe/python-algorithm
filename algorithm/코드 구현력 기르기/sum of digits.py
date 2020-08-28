'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
각 자연수의 자릿수의 합을 구하는 함수 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.
'''

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
nums = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x != 0:
        sum += x % 10
        x //= 10
    return sum


result = max = 0
for n in nums:
    sum = digit_sum(n)
    if max < sum:
        max = sum
        result = n

print(result)


# 강의 중 강사님 코드
import sys
sys.stdin = open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))


def degit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum


# string으로 처리하는 방법도 있다!
def degit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum


max = -2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)
