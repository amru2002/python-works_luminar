from json import load
path=("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\modules\\read_fromjson\\movies\\countries\\countries.json")
with open(path,encoding="utf-8") as f:
    country=load(f)

# print total
print(len(country))
# # print all countries name
# countries_name=[c.get("name")for c in country]
# print(countries_name)
# # printcounrty name capital is Mariehamn
# capital=[c.get("name") for c in country if c.get("capital")=="Mariehamn"]
# print(capital)
# print langues used portugues coutry name
# langu=[ c.get("name")for c in country for l in c.get("languages") if l.get("nativeName")=="English"]
# print(langu)
# print county name whose region="Europe"
# reg=[c.get("name")for c in country if c.get("region")=="Europe"]
# print(reg)
            
# print highest population coutry name
# popu=max(country,key=lambda c:(c.get("population")))
# print(popu)

# print all Borders
# bor={ b for c in country for b in c.get("borders")}
# print(bor)
# country name starts with c
# starts_withc=[c.get("name")for c in country if c.get("name").startswith("C")]
# print(starts_withc)
# # print all name and capital of countries
# name_capital=[[c.get("name"),c.get("capital")]for c in country]
# print(name_capital)
# print borders share maximum country
# c_with_borders=[c for c in country if "borders" in c]
# max_border=max(c_with_borders,key=lambda c:len(c.get("borders")))
# print(max_border.get("name"))
# india_borders=[c.get("borders")for c in country if c.get("name")=="India"][0]
# print(india_borders)
# border_name=[c.get("name")for c in country if c.get("alpha3Code")in india_borders]
# print(border_name)
#  all region names
# region={ c.get("region") for c in country }
# print(region)
# # independent country
# dependent=[c.get("name")for c in country if c.get("independent")==False]
# print(dependent)
# population less tha 4k
# pop=[c.get("name")for c in country if c.get("population")<40000]
# print(pop)
#print  region vise count for all countries
wc={}
for c in country:
    region=c.get("region")
    if region in wc:
     wc[region]+=1
    else:
      wc[region]=1
print(wc)




