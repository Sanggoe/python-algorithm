'''
대표값
N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중
평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요. 답이 2개일 경우 성적이 높은
학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.
'''

# 내가 짠 코드
import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
students = list(map(int, input().split()))
avg = int(sum(students) / N + 0.5)
index = 0

for i in range(1, N):
    if abs(students[i] - avg) < abs(students[index] - avg):
        index = i
    elif abs(students[i] - avg) == abs(students[index] - avg):
        if students[i] > students[index]:
            index = i

print(avg, index + 1)



# 내가 짠 코드 2회차
import sys

sys.stdin = open("input.txt", "r")
N = int(input())
nums = list(map(int, input().split()))
avg = int(sum(nums) / N + 0.5)
min = 1

for i, v in enumerate(nums):
    if abs(avg - v) < abs(avg - nums[min]):
        min = i
    elif abs(avg - v) == abs(avg - nums[min]):
        if v > nums[min]:
            min = i

print(avg, min + 1)



# 강의 중 강사님 코드
import sys

sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a) / n)
# round : round_half_even 방식의 반올림 함수. 정확하게 절반일 땐 자연수 짝수에 가까운 근사값으로 만든다.
# 따라서 round
min = 2147000000

for idx, x in enumerate(a):  # enumerate : index값 반환
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
