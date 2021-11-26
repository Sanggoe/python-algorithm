N = int(input("금액 : "))
unit = [500,100,50,10]
total = 0

for i in unit:
    print("{}원 : {}개".format(i, N//i))
    N %= i
