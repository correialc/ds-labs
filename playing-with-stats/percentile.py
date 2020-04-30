import math

def my_percentile(sample, pos):
    l = (pos/100)*len(sample)
    if (l.is_integer()):
        l = int(l)
        p = (sample[l-1]+sample[l])/2
    else:
        p = sample[int(math.ceil(l))-1]
    
    return int(p)

mysample = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]

# 3rd quartile
p75 = my_percentile(mysample, 75)
print(p75)

# 4rd decile
p40 = my_percentile(mysample, 40)
print(p40) 

# 10th percentile
p10 = my_percentile(mysample, 10)
print(p10)

# 80th percentile
p80 = my_percentile(mysample,80)
print(p80)