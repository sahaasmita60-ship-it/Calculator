print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for remainder")
print("Enter 6 for exponent")

a=int(input("Enter the number for the operation you want to perform: "))
print("Now enter the two numbers you want to perform your selected operation on: ")
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
ans=0
if(a==1):
    ans=n1+n2
elif(a==2):
    if(n1>n2):
        ans=n1-n2
    else:
        ans=n2-n1
elif(a==3):
   ans=n1*n2
elif(a==4):
    ans=n1/n2
elif(a==5):
    ans=n1%n2 
else:
    ans=n1**n2
print(ans)