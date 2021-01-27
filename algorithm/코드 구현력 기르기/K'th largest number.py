'''
K번째 큰 수
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다.
현수는 이 중 3장을 뽑아각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다.
기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.

만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.
'''


# 내가 짠 코드
import sys
sys.stdin=open("input.txt", "rt")

N, K = map(int, input().split())
a = list(map(int, input().split()))
sum = list()

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum.append(a[i]+a[j]+a[k])

sum.sort(reverse=True)

for i in range(len(sum)+1):
    if i == 0 :
        K-=1
    elif sum[i] != sum[i-1]:
        K-=1
    else :
        continue
    if not K :
        print(sum[i])
        break



# 내가 짠 코드 2회차
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
N, K = map(int, input().split())
nums = list(map(int, input().split()))
results = list()
for i in combinations(nums, 3):
    results.append(sum(i))

print(sorted(results, reverse=True)[K-1])



# 강의 중 강사님 코드
import sys
sys.stdin=open("input.txt", "rt")

N, K = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            res.add(a[i]+a[j]+a[k])
res=list(res)
res.sort(reverse=True)
print(res[K-1])