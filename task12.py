n = int(input("enter the rows:"))
i = 0
h = "--- "
v = "|   "
h = h * n
v = v*(n+1)
while (i < n+1):
    print (h)
    if(i != n):
        print (v)
    i+=1
