a=int(input("enter a number:"))
for i in range(a):
    if a>=1:
        i*=a
        a-=1
        
print("factorial of number",i)