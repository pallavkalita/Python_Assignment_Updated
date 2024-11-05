# Understanding the concept of deep copy using python program


import copy

original = [[1, 2], [3, 4]]

deep_copy = copy.deepcopy(original)

deep_copy[0][1] = 99

print(original)
print(deep_copy)
