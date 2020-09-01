'''
회문 문자열 검사
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우
(회문 문자열)이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을
작성한다. 단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''

# My code
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
for _ in range(n):
    str = list(input().lower())
    length = len(str)
    for i in range(length // 2):
        if str[i] != str[length - 1 - i]:
            print("#", _ + 1, " NO", sep="")
            break
    else:
        print("#", _ + 1, " YES", sep="")

# Teacher's code
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    # 문자열을 거꾸로 뒤에서부터 보는 방법
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" % (i + 1))

'''
    size = len(s)
    for j in range(size // 2):
        # 파이썬에서는 index에 뒤에서부터 -1부터, 음수로 접근하는 방법도 있다!!
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

for i in range(n):
'''