print('**********Hey Gunjan Your Calculation is here you can start*********')


def calculate(Amount=n):

 Amount = int(input('Enter Your Amount: '))

 c = Amount/1.18
 print("Your GST AMOUNT: ",int(Amount-c))
 print("Your core Amount is : ",int(c))
 print("your total policy is ",int(c/720))

n = 2

if n == 2:
    
    calculate()
else:
    print("enter correct num so we can proseed you calculation")
