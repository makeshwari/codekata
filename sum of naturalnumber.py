n=int(input())
if n < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(n > 0):
       sum += n
       n -= 1
   print("The sum is",sum)
