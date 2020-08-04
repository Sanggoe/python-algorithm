'''
최솟값 구하기
'''

# 내가 짠 코드
arr = [5,3,7,9,2,5,2,6]
min = arr[0] # 표현 가능한 가장 큰 값
for i in arr:
    if i < min :
        min = i
print(min)


# 강의 중 강사님 코드
arr = [5,3,7,9,2,5,2,6]
min = float('inf') # 표현 가능한 가장 큰 값
for i in range(len(arr)):
    if arr[i] < min :
        min = arr[i]
print(min)