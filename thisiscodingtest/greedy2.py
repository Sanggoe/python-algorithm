N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

max_num = max(nums)
nums.remove(max_num)
second_num = max(nums)


_k = 0
for i in range(0, M):
   if K == _k:
       _k = 0
       result += second_num
   else:
       result += max_num
       _k += 1

print(result)


'''
c = 0
for i in range(0, M):
    if ( (i+c) % K == 0 ):
        result += second_num
        c += 1
    else:
        result += max_num
'''
