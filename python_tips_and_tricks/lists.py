"""
Common tips and tricks dealing with lists.
"""

# To sort a collection
# Use the built-in sort function
names = ["Ben", "Andrew", "Ashley"]

print(sorted(names))

# To sort a collection backwards
print(sorted(names, reverse=True))

# To loop a sorted collection with a custom sort order
# Use a key function
# Key function is called once per key
print(sorted(names, key=len))
