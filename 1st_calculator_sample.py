


A=[0]
while True:
    b = int(input())
    A.append(b)
    print(A)
    operator = input('enter oprator')
    print(operator) 
    if operator == '+':
        sum = A[0] + A[1]
        print(sum)
        A.clear()
        A.append(sum)
        print(A)
    elif operator == '-':
        sum = A[0] - A[1]
        print(sum)
        A.clear()
        A.append(sum)
        print(A)
    elif operator == '*':
        sum = A[0] * A[1]
        print(sum)
        A.clear()
        A.append(sum)
        print(A)
    elif operator == '/':
        sum = A[0] / A[1]
        print(sum)
        A.clear()
        A.append(sum)
        print(A)
    else:
        print(A)
        

    
