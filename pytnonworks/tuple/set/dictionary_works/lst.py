lst=[2,3,4,5,7]
#    0 1  2 3
sum=9
lst.sort()
low=0
upper=len(lst)-1
while(low<upper):
    current_sum=lst[low]+lst[upper]
    if current_sum==sum:
        print("pairs",lst[low],lst[upper])
        break     #low+=1(all pairs)
    elif current_sum<sum:
            low+=1
    else:
            upper-=1



    

