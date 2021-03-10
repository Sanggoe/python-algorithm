'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
가장 높은 확률로 나올 수 있는 숫자의 합을 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''

# 내가 짠 코드
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
cnt = [0] * (N+M)

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j-1]+=1

max = max(cnt)
for index, count in enumerate(cnt):
    if max == count:
        print(index + 1, end=" ")



# 내가 짠 코드 2회차
import sys

sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
nums = sorted([i + j for i in range(1, N+1) for j in range(1, M+1)])
max = 0
res = list()
for n in set(nums):
    count = nums.count(n)
    if max < count:
        res = [n]
        max = count
    elif max == count:
        res.append(n)

for n in sorted(res):
    print(n, end=" ")


# 강의 중 강사님 코드
import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0] * (n+m+3)
max = -2147000000

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')