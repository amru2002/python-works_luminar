from json import load
path=("C:\\Users\\amrutha\\Desktop\\pytnonworks\\list_works\\file_inputoutput\\modules\\read_fromjson\\data.json")
with open(path) as f:   # (pat,encoding=utf-8)error
    records=load(f)
print(records)

fw_names=[f.get("name")for f in records]
print(fw_names)

fw_top=max(records,key=lambda d:d.get("rating"))
print(fw_top)

# frontend,python framework names
fra_names=[f.get("name")for f in records if f.get("language")=="python"]
print(fra_names)

fra_names=[f.get("name")for f in records if f.get("side")=="frontend"]
print(fra_names)

