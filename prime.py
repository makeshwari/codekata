x=0
a=int(input("enter:"))
for i in range(2,int(a/2)):
 if a%i==0:
   x=1
   break
if(x==1):
 print("no")
else: 
 print("yes")  
