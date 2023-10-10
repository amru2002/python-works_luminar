
lst=[3,1,5,6,4]
lst.sort()
for i in range(0,len(lst)):
    current=lst[i]
    next=lst[i+1]
    diff=next-current
    if diff!=1:
     print (current+1,"is missing" )
     break


lst=[3,1,5,6,4] # [1,3,4,5,6]
lst.sort()        # 0 1 2 3 4
for i in range(0,len(lst)):
   current=lst[i]
   next=lst[i+1]
   diff=next-current
   if diff!=1:
      print(current+1,"is missing")
      break