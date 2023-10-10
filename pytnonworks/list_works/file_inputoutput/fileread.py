# f=open("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\data.txt","r")
# lst=[]
# for line in f:
#     print(line)      words=[line.rstrip("\n")for line in f]
                       # lon_wrd=max(lst,key=lambda w:len(w))
                      # print(long_wrd)
# to add new list 
# for line in f:
#     lst.append(line.rstrip("\n"))
# print(lst)
# long_wrd=max(lst,key=lambda w:len(w))
# print(long_wrd)

f_read=open("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\data.txt")
odd_write=open("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\odd.txt","w")
even_write=open("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\even.txt","w")
for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_write.write(str(num)+"\n")
    else:
        odd_write.write(str(num)+"\n")
