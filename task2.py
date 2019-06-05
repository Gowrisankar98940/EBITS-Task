a=int(input("Enter the number:"))
b=int(input("enter the divide num:"))
if(a%4==0):
    print('divide by four')
elif(a%2==0):
    print('even num')
else:
    print('ood num')
if(a%b==0):
    print(a,"divides evenly by",b)
else:
    print(a,"not divides evenly by",b)

