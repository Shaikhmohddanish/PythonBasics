num=int(input("Enter number of Rows: "))
for i in range(0,num):
    for j in range(num,i,-1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print(" * ",end=" ")
    print()
# num=int(input("Enter no of rows: "))
for i in range(0,num+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(num+1,i,-1):
        print(" * ",end=" ")
    print()