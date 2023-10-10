def num(num1,num2):
    for num in range(1,(num2+1)):
        if(num1%num==0)and(num2%num==0):
            hcf=num
    print(hcf)
num(24,18)