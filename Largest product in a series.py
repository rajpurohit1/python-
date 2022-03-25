def main():
 num = str(7316717653133062491922511967442657474235534919493)
 largest_num = 0
 current = 1
 how_many_digit = 3
 for i in range(len(num)-how_many_digit):
     print(i,"..............iiiii")
     for j in range(how_many_digit):
         print(j,"..............jjjj")
         
         current *= int(num[i+j])
         #print(current)
     if current > largest_num:
         largest_num = current
     current = 1
 print(largest_num)
main()