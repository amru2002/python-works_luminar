# Question (1)
num=int(input("enter a number "))
if(num>=10 and num<=20):
       print("thank you")
else:
      print("incorrect")
#qu(2)
num=int(input("enter a number"))
if (num<10):
    print("To low")
elif(num>=10 and num<=20):
    print("correct")
else:
    print("To high")
# QS(3)
age=int(input("enter the age"))
if (age>=18):
    print("you can vote")
elif(age==17):
    print("you can learn to drive")
elif(age==16):
    print("you can buy a lottary ticket")
elif(age<16):
    print("you can go for treat")
# QS(4)
num=int(input("enter the num 1,2,or 3"))
if (num==1):
    print("Thank you")
elif(num==2):
    print("well done")
elif(num==3):
    print("correct")
else:
    print("Error message")
# QS(5)
num=int(input("enter a number"))
if(num%2==0 and num%3==0):
 print("the num is divisible")
else:
 print("not divisible")
# QS(6)
ch=input("enter a character")
if (ch=="a")or(ch=="e")or(ch=="i")or(ch=="o")or (ch=="u"):
    print("vowel")
else:
    print("not vowel")
# QS(7)
num=int(input("enter a number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
# QS(8)
start=1
end=20
while(start<=end):
    if start%2==0:
        print(start)
    start+=1
# QS(9)
name=input("enter the name")
start=1
end=3
while(start<=end):
    print(name)
    start+=1
# QS(10)
name=input("enter the name")
num=int(input("enter a number"))
  
for i in range(num):
  if (num<10):
   print(name)
  else:
    print("To high")
    break

# QS(11)
num=int(input("how many people do yo want to invite to a party"))
if(num<10):
    name=input("enter your name")
    print(name,"has been invited")
else:
    print("too many people")
# QS(12)
num=0
while(num<=5):
    num=int(input("enter a number"))
    print("the last number  you entered is ",num)
# QS(13)
while(True):
 num=int(input("enter a number between 10 and 20"))
 if(num<10):
    print("To low")
 elif(num>20):
     print("To high")
 else:
    print("thank you")
    break
#  QS(14)
start=10
end=300
while(start<=end):
    print(start)
    start+=10
# QS(15)
avg=0
total=0
for avg in range(5):
    n=int(input("enter a number"))
    total=total+n
avg=total/5
print(avg)


        
        