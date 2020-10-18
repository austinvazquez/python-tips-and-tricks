"""
Common tips and tricks with dictionaries.
"""

from collections import defaultdict


d = {"Ben": "red", "Andrew": "Blue", "Ashley": "Yellow"}

# When looping over dictionary keys
# Use for key in dict for non-mutable cases
for key in d:
    print(key)

# For mutating, reinstantiate the dictionary.
d = {key: d[key] for key in d if not key.startswith("B")}

# When looping over a dictionary's key and values
for key, value in d.items():
    print(f"{key} likes {value}")

# Constructing a dictionary from lists.
names = ["Ben", "Andrew", "Ashley"]
colors = ["Red", "Blue", "Yellow"]

d = dict(zip(names, colors))
print(d)

d = dict(enumerate(names))
print(d)

# Counting with dictionaries.
d = defaultdict(int)
for color in colors:
    d[color] += 1

print(d)

# Grouping with dictionaries.
d = defaultdict(list)
for name in names:
    d[len(name)].append(name)

print(d)
