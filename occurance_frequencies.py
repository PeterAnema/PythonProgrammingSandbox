# Get occurance frequency of list elements

values = [1,9,2,9,7,4,6,3,2,4,7,9,8,4,3,1,2,3,3,3,3,3,3,3,3,3,14]
print(values)


resultvalues = {value: values.count(value) for value in set(values)}


resultvalues = [[value, values.count(value)] for value in set(values)]


resultvalues = [(value, values.count(value)) for value in range(min(values), max(values)+1)]
for item in resultvalues:
    print("%3d: %s" % (item[0], "*" * item[1]))
