
def push(a,var):
    a.append(var)
    print("element pushed successfuly")
def poptime(a):
    
   var = a.pop()
   print("deleted",var)
   
def peek(a):
    index = len(a)-1
    print("last element is:",a[index])
    
def display(a):
      for i in range(len(a)-1,-1,-1):
        print(a[i]) 
   
a = []
while True:
    choice = int(input("1.push\n2.push\n3.delete\n4.peek\n5.exit\nEnter your chocie: "))
    if choice == 1:
        var = int(input())
        push(a,var)
    elif choice == 2:
        if len(a) == 0:
            print("stack is empty")
        else:
            poptime(a)
    elif choice == 3:
        if len(a) == 0:
            print("stack is empty")
        else:
            peek(a)
    elif choice == 4:
         if len(a) == 0:
             print("stack is empty")
         else:
             display(a)
    else:
        break
         