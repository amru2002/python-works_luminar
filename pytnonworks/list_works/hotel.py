foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]
 #total number of items
# print(len(foods))
# # print name whose category = veg
# cat=[f.get("name")for f in foods if f.get("category")=="veg"]
# print(cat)
# # food names available under rs 100
# price=[f.get("name")for f in foods if f.get("price")<100]
# print(price)

# # costly item
# item_cost=max(foods,key=lambda f:f.get("price"))
# print(item_cost)
# costly non-veg food
# cost_nonveg=[f for f in foods if f.get("category")=="non-veg"]
# cost=max(cost_nonveg,key=lambda f:f.get("price"))
# print(cost)
# ptint all categories
categories={f.get("category")for f in foods}
print(categories)


