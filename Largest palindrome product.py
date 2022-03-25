

sum = 1

 for i in range(10,99): 
    c = i*(i+1) 
     while (c>0):
       
    
      d = (c%10)
      sum = (sum*10)+d
      c=c//10;
   if sum == c:
     print(c)
   
sum = 1

    