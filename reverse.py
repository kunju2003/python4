n=int(input("enter number:"))
r=0
for i in range (1,n):
    if n>0:  
      rem=n%10
      r=(r*10)+rem
      n=n//10

print("reverse of number",r)
