text="sunil gavaskar had a no-hold-barred remark on overseas commentators"
# print word to start with vowels
words=text.split(" ")
vowels=("a","e","i","o","u")
for w in words:
    if w.casefold().startswith(vowels):
        print(w)
