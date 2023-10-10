def count (val):
    v_count=0
    c_count=0
    for i in range(len(val)):
     if val[i] in("a","e","i","o","u"):
        v_count+=1
    else:
        c_count+=1
    print(v_count)
    print(c_count)
val=input("enter a name")
count(val)
