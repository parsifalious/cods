n=int(input())
a=[0]*n
counter=0
for i in range(n):
    a[i]=input()
for i in range (n):
    if a[i]=="0" or a[i]=="False" or a[i]=="false" or  a[i]=="None":
        counter+=1
if (counter>0):
    print ("False")
else:
    print("True")
