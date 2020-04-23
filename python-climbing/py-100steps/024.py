mydict = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# Without lambda
for (k,v) in mydict.items():
    print(k + " has value {0}".format(v))