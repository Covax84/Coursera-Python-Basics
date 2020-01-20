n = int(input())
h = n // 3600 % 24
m1 = n // 60 % 60 // 10
m2 = n // 60 % 60 % 10
s1 = n % 60 // 10
s2 = n % 60 % 10
print(str(h), str(m1)+str(m2), str(s1)+str(s2), sep=':')
