class listnode(object):
 def_init_(self,y):
  self.value=y
  self.next=none
class solution(object):
 def addTwoNumber(self,11,12):
  carry=0
  head=curr=listnode(0)
  while 11 or 12
   value=carry
   if 11:
    value+=11.value
    11=11.value
   if 12:
    value+=12.value
    12=12.next
   curr.next=listnode(value%10)
   curr+curr.next
   carry=value/10
  if carry>0:
   curr.next=listnode(carry)
  return head.next 
   
