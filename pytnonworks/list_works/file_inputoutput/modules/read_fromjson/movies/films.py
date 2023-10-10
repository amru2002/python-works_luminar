from json import load
path=("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\modules\\read_fromjson\\movies\\mdb.json")
with open(path,encoding="utf-8") as f:
    movies=load(f)
# print(len(movies))
# print all movies name
# movies_name=[ m.get("title")for m in movies]
# print(movies_name)
# # print movie title released in 2005
# movies_name=[m.get("title")for m in movies if m.get("year")=="2005"]
# print(movies_name)
# # print movie title whose genre="comedy"
# genre=[m.get("title")for m in movies if "Comedy" in m.get("genres")]
# print(genre)
# lengthly movie title
lengthly=max(movies,key=lambda m:int(m.get("runtime")))
print(lengthly)
# print all genres
all_genres={g for m in movies for g in m.get("genres") }
print(all_genres)

comedy=[ m.get("title")for m in movies if "Comedy" in m.get("genres")and m.get("year")=="2015"]
print(comedy)

wc={}
for m in movies:
    year=m.get("year")
    wc[year]+=1
else:
    wc[year]=1
ye=max(wc,lambda k:m.get(k))