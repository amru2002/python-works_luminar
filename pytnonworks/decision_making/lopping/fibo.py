# limit=24
# prev=0
# curent=1

# print(prev)
# print(curent)
# for i in range(1,limit+1):
#     sum=prev+curent
#     prev=curent
#     curent=sum
#     if sum <=limit:
#         print(sum)
#     else:
#         break
limit=8
prev=0
current=1
sum=0
print(prev)
print(current)
for num in range(1,limit+1):
    sum=prev+current
    prev=current
    current=sum
    if(sum<=limit):
        print(sum)
    else:
        break


    

