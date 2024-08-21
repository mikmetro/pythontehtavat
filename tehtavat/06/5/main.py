def parilliset(l):
    lt = []
    for i in l:
        if i % 2 == 0:
            lt.append(i)
    return lt

list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(parilliset(list))
