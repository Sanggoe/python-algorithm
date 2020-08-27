'''
중첩 반복문(2중 for문)

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print();

for i in range(5):
    for j in range(i):
        for k in range(j):
            print("*", end=" ")
        print();  
'''
n = 3

for i in range(n): # 삼각형을 한줄로 봤을때 줄 수
    for row in range(1, n): # 삼각형의 실제 별의 줄 수 n-1 개만큼
        for repeat in range(i+1): # 가로로 몇 번 반복되는지
            for column in range(row): # 별 출력
                print("*", end=" ")
            for blank in range(n-row): # 공백 출력
                print("  ", end="")
        print() # 엔터
