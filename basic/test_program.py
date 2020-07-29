str1="a234"
str2="1234"

answer=True;

print(len(str2))
if len(str1) != 4 and 6:
    answer = False
print(answer)
    
if not all(i.isdecimal() for i in str2):
    answer = False

print(answer)
