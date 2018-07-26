def product(*x):
    if len(x) == 0:
        raise TypeError
    else:
        global sum
        sum = 1
        for i in x:
            sum = i *sum
    return sum
print(product(5,6,7))
print(product())