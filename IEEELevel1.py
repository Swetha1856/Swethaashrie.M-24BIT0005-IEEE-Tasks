def push(x,lt):
    lt.append(x)
    print("The resultant stack: ")
    for i2 in lst:
        print(i2)
def pop(lt):
    print("The resultant stack: ")
    lst.remove(lst[0])
    for j2 in lst:
        print(j2)
def top(lt):
    print("The Topmost element: ",lst[0])
def getMin(lt):
    min=lst[0]
    for i in lst:
        if(i<min):
            min=i
    print("The Smallest element: ",min)
def getMax(lt):
    max=lst[0]
    for i in lst:
        if(i>max):
            max=i
    print("The Largest element: ",max)
lst=[]
len=int(input("Number of elements in list: "))
print("Enter elements: ")
for i in range(len):
    lst.append(int(input()))
ch="y"
while(ch=="y"):
    print("MENU")
    print("1.Pushes element")
    print("2.Removes topmost element")
    print("3.Returns topmost element without removing it")
    print("4.Returns smallest element")
    print("5.Returns largest element")
    n=int(input("Enter your choice: "))
    if(n==1):
        print("The original stack: ")
        for i1 in lst:
            print(i1)
        elem=int(input("Enter the push element: "))
        push(elem,lst)
    elif(n==2):
        print("The original stack: ")
        for j1 in lst:
            print(j1)
        pop(lst)
    elif(n==3):
        print("The original stack: ")
        for k1 in lst:
            print(k1)
        top(lst)
    elif(n==4):
        print("The original stack: ")
        for l1 in lst:
            print(l1)
        getMin(lst)
    elif(n==5):
        print("The original stack: ")
        for m1 in lst:
            print(m1)
        getMax(lst)
    ch=input("Do you want to continue making changes?(y/n)")
    if(ch=="n"):
        break
    elif(ch=="y"):
        continue
    elif(ch!="n" or ch!="y"):
        print("Invalid Input")
        break

