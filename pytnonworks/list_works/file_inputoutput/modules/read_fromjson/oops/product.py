def product(*args):
    res=1
    for num in args:
        res*=num
    return res
print(product(1,2,3,4,5))