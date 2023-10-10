number=int(input("enter number>"))
original=number
digit_count=len(str(number))
sum=0
while(number!=0):
    last_digit=number%10
    exponent=last_digit**digit_count
    print(exponent)
    sum=sum+exponent
    number=number//10
print("armstrong number" if sum==original else "not armstrong")
