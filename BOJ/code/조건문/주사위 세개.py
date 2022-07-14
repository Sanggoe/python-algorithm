s1, s2, s3 = map(int, input().split())
if s1==s2==s3:
  print(10000+s1*1000)
elif s1==s2 or s1==s3:
  print(1000+s1*100)
elif s2==s3:
  print(1000+s3*100)
else:
  print(max(s1,s2,s3)*100)