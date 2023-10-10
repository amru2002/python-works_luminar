# lst=[2,1,5,3,6,3]
# lst.sort()
# for i in range(0,len(lst)-1):
#     current=lst[i]
#     next=lst[i+1]
#     if current==next:
#       print(current)


lst=[2,1,5,3,6,3,3,5,6]
lst.sort()
duplicate_list=[]
for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]
    if current==next:
      if current not in duplicate_list:
        duplicate_list.append(current)
print(duplicate_list)

# colors      
colors=["red","green","black"]
if "yellow" in colors:
   print(colors)



# lst=[2,1,5,3,6,3,3,5,6]
# lst.sort()
# duplicate_list=[]
# for i in range(0,len(lst)-1):
#    current=lst[i]
#    next=lst[i+1]
#    if current==next:
#       if current not in duplicate_list:
#         duplicate_list.append(current)
#       print(duplicate_list)