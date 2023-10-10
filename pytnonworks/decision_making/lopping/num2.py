start=1
end=50
while(start<=end):
    if (start%3==0):
        print("a")
    elif(start%5==0):
        print("cd")
    elif(start%15==0):
        print("ef")
    else:
        print(start)
    start+=1
