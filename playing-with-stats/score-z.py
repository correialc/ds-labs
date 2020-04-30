from statistics import stdev , mean

my_scorez = lambda sample, element : (element - mean(sample))/stdev(sample)

s = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]

# Applying
print(my_scorez(s, s[0]))  # Most distant below the mean
print(my_scorez(s, s[11])) # Most distant above the mean 

# Inverting
print(stdev(s) + mean(s))   # 1 std above the mean
print(mean(s) - stdev(s)/2) # 0.5 std below the mean