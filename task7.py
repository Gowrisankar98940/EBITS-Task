
a=0
b=1
i=0
n=int(input("Enter the number:"))
while(i < n):
    if i <= 1:
        c = i
    else:
        c=a+b
        a=b
        b=c
    i=i+1
    print('serious are:',c)
