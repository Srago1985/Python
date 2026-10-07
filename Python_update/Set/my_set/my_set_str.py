from my_set import MySet

set_of_strings = MySet()

print(set_of_strings.add("apple"))
print(set_of_strings.add("banana"))
print(set_of_strings.add("apple"))

print(len(set_of_strings))

for string in set_of_strings:
    print(string)