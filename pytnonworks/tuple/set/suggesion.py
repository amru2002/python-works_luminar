all_users={"sachin","dhoni","kohli","rohit","sanju","padikkal"}
sanju_followings={"padikkal","sachin"}
suggestion=list(set(all_users).difference(set(sanju_followings)))
# sanju_pos=suggestion.index("sanju")
suggestion.pop(suggestion.index("sanju"))
print(suggestion)


