def display_emp(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("salary"))
display_emp(name="hari",dep="hr",n_place="erk",salary=24000)