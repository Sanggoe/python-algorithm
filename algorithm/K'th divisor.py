'''
K번째 약수
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
'''

# 내가 구현한 코드
# 파일 입출력으로 입력받기
import sys
sys.stdin=open("input.txt", "rt") # 파일 이름

N, K = map(int, input().split())

for i in range(1, N+1):
   if not N%i:
       K-=1
       if not K:
           print(i)
           break
else: print(-1)

# 강의 중 강사님의 코드
'''
N, K = map(int, input().split())
cnt=0
for i in range(1, N+1):
   if not N%i:
       cnt+=1
   if cnt==K:
       print(i)
       break
else: print(-1)
'''