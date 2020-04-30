import math

def my_std(sample):
    smean = (sum(sample)/len(sample))
    stdsum = 0

    for n in sample:
        stdsum = stdsum + (n-smean)**2

    return math.sqrt(stdsum/(len(sample)-1))

s = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]
print(my_std(s))