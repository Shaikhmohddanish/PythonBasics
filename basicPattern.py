num=int(input("Enter number of Rows: "))
for i in range(0,num):
    for j in range(num,i,-1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print(" * ",end=" ")
    print()