lst=[2,3,4,5,6,7,8]
# squres=[]
# # for n in lst:
#     sq=n**3
#     squres.append(sq)
# print(squres)
# list comprehsion(return,loop ,condition)

cubes=[n**3 for n in lst]
print(cubes)

squres=[n**2 for n in lst]
print(squres)

# add 2 in lst
add_two=[n+2 for n in lst]
print(add_two)


# condition
# print even nums
evens=[n for n in lst if n%2==0]
print(evens)

# print odd
odds=[n for n in lst if n%2!=0]
print(odds)
# print num>5
great=[n for n in lst if n>5]
print(great)

# years return from 1800-2025
years=[y for y in range(1800,2025)]
print(years)
# century_year
# century_year=[y for y in years if y%100==0]
# print(century_year)

noncentury_year=[y for y in years if y%100!=0]
print(noncentury_year)
