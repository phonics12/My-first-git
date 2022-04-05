s=[1,1]
n=int(input("숫자를 입력: "))
for i in range(2,n+1):
    s.append(s[i-2]+s[i-1])
print(s[n-1])