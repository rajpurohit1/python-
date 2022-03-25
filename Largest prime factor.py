n = int(input())
a = 2
b = []
while (a<n):
    if n%a==0:
        n=n//a
        b.append(a)
        #a = a+1
    else:
        a = a+1
print(b)
    
