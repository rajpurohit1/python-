a = int(input())
n = 11
 
while n>0:
 for i in range(1,a):
     c = i*n
     if ((c%1==0) and (c%2==0) and (c%3==0) and (c%4==0) and (c%5==0) and (c%6==0) and (c%7==0) and (c%8==0) and (c%9==0) and (c%10==0) ):
         print(c)
         n = 0
         break
     else:
         n = n+1
print('ishwar')         
    
