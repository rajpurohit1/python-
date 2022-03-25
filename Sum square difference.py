
sum = 0
b = 0

for i in range(1,11):
    a = i**2
    b = i+b
    sum = sum + a
b = (b**2)-sum

print(b)    
print(sum)
