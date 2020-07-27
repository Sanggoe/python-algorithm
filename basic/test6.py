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

n = 5
for i in range(n):
    for row in range(1, n):
        for repeat in range(i+1):
            for column in range(row):
                print("*", end=" ")
            for blank in range(n-row):
                print("  ", end="")
        print()    
'''

