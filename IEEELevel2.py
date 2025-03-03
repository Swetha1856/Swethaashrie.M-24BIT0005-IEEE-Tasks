def addInterval(start,end,lst1):
    lst1.append([start,end])#Im adding all the intervals to lst1
    lst1.sort()#Here im sorting each interval based on the start value of the interval given by user
    nlst=[]
    for i in lst1:
        if nlst and i[0]<=nlst[-1][1]:#nlst[-1][1] is the end of the last interval and i[0] is the start of the new interval given by user.Here i am checking if they are overlapping or not.
            nlst[-1][1]=max(nlst[-1][1],i[1])#if they do overlap, i am updating the new list's end value with the max of nlst[-1][1] and (i[1] which is the end of the new interval)
        else:
            nlst.append(i)#if it doesnt overlap, im updating the new list
    return nlst
def getIntervals(tot):
    print(tot)
lst=[]
ch="y"  
res=[]
while(ch=="y"):
    print("MENU")
    print("1.Add intervals")
    print("2.Get intervals")
    n=int(input("Enter your choice: "))
    if(n==1):
        c=int(input("Enter start of interval: "))
        d=int(input("Enter end of interval: "))
        lst=addInterval(c,d,lst)
    elif(n==2):
        getIntervals(lst)
    else:
        print("Invalid Input")
    ch=input("Do you want to continue?(y/n): ")
