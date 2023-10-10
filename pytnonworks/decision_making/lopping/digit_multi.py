num=371
original=num
sum=0
while (num!=0):
   last_digit=num%10
   cube=last_digit**4
   sum=sum+cube
   num=num//10
if(original==sum):
   print("armstrong num")
else:
   print("not armstrong")





















