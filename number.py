class listnode(object):
 def_init_(self,y):
  self.val=y
  self.next=none
class solution(object):
 def addTwoNumber(self,11,12):
  carry=0
  head=curr=listnode(0)
  while 11 or 12
   val=carry
   if 11:
    val+=11.val
    11=11.val
   if 12:
    val+=12.val
    12=12.next
   curr.next=listnode(val%10)
   curr+curr.next
   carry=val/10
  if carry>0:
   curr.next=listnode(carry)
  return head.next 
   
