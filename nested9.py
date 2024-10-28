nsum=0
esum=0
osum=0
for i in range(21):
    nsum+=i
    if i%2==0:
        esum+=i
    elif i%2!=0:
        osum+=i  
print("sum of natural numbers",nsum) 
print("sum of even numbers",esum)  
print("sum of odd numbers",osum)     
