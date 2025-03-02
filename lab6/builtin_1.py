n=int(input())
a=[0]*n
sum=1
for i in range(n):
    a[i]=int(input())
for i in range(n):
    sum*=a[i]
print (sum)


