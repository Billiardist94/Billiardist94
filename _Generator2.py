def chain(it1, it2, it3):
    return list(it1) + list(it2) + list(it3)


for x in chain(range(3), range(1, 4), range(2, 5)):
    print(x, end=', ')
