d = {"a":1, "b":2, "c":3}
print(dict({key:value for (key,value) in d.items() if value <=1})) # Dict comprehension
print(dict(filter(lambda item: item[1] <= 1, d.items()))) # Filter