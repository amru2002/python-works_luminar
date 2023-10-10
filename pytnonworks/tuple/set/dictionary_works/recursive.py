text="ABCDA"
wc={}
for ch in text:
    if ch in wc:
        print("first recursive",ch)
    else:
        wc[ch]=1

text="ABCDA"
wc={}
for ch in text:
    if ch in wc:
        print("first recursiveo is",ch)
        break
    else:
        wc[ch]=1
        # print(wc)

        


