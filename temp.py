def iloczyn(*arg):
    ilocz = 1
    for x in arg:
        ilocz *= x
    # return ilocz
    print(ilocz)


iloczyn(2, 4, 5)
iloczyn(2, 4, 5, 6)
iloczyn(*range(6))
