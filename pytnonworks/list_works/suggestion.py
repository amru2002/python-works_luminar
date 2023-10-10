# all_users=["mohanlal","fahad","unny","mamooty","nivin"]
# nivin_friends=["mohanlal","fahad","unny"]
# for u in all_users:
#     if u not in nivin_friends :
#      print(u)

# add suggesion_list
all_users=["mohanlal","fahad","unny","mamooty","nivin"]
nivin_friends=["mohanlal","fahad","unny"]
suggesion_list=[]
for u in all_users:
    if u not in nivin_friends :
     suggesion_list.append(u)
suggesion_list.pop(suggesion_list. index("nivin"))
print(suggesion_list)