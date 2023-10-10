text="ABABBCDCEF"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
        for k,v in wc.items():
            v==1
            print(k)
        
    