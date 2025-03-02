a=input()
palindrome=False
for i in range(int(len(a))//2):
    if a[i]==a[len(a)-i-1]:
        palindrome=True
if palindrome==True:
    print("Its palindrome")
else:
    print("Its not palindrome")