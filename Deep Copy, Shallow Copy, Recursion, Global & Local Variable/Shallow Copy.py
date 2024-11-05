# Understanding the concept of shallow copy using python program


import copy

original = [[1, 2], [3, 4]]

deep_copy = copy.copy(original)

deep_copy[0][1] = 99

print(original)
print(deep_copy)
