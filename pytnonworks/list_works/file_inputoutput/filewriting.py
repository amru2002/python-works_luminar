f=open("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\data1.txt","r")
lst=[]
for line in f:
    lst.append(line.rstrip("\n"))
print(lst)