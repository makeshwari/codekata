sum=0
num=int(input(""))
while(num>0):
 digit=num%10
 sum+=digit**3
 num=num/10
if sum==num:
 print("YES")
else:
 print("NO")
 
 
