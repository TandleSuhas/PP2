a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))

if(a>b and a>c):
    print(a," is greater among three ")
elif(b>a and b>c):
    print(b," is greater among three ")
else:
    print(c," is greater among three ")
