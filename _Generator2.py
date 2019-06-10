def chain(it1, it2, it3):

    for x in range(it1):
        print(x)
    print()
    for y in range(*it2):
        print(y)
    print()
    for z in range(*it3):
        print(z)

chain(3, (1, 4), (2, 5))