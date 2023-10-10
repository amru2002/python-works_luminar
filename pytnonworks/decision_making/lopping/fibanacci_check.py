 
num=int(input("enter a number"))
prev=0 
current=1
start=1
fib_num=0
print(prev)
print(current)
is_fibo=False
while(start<=num):
    fib_num=prev+current
    print(fib_num)
    prev=current
    current=fib_num
    if(fib_num==num):
        is_fibo=True
        break
    start+=1

  
