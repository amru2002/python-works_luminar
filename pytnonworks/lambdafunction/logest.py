# text="hi hello good hello goodmorning"
# words=text.split(" ")
# longest_word=max(words,key=lambda w:len(w))
# print(longest_word)
# # smallest_word
        
# small_word=min(words,key=lambda w:len(w))
# print(small_word)

# # sorted form
# srt_word=sorted(words,key=lambda w:len(w),reverse=True)
# print(srt_word)
text="hai hello have goodmornig"
word=text.split(" ")
lon=max(word,key=lambda w:len(w))
print(lon)
sma=min(word,key=lambda w:len(w))
print(sma)
sor=sorted(word,key=lambda w:len(w),reverse=True)
print(sor)