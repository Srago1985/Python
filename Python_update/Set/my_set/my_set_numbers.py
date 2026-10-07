from my_set import MySet

set_of_numbers = MySet()

print(set_of_numbers.add(10))
print(set_of_numbers.add(20))
print(set_of_numbers.add(10))

print(len(set_of_numbers))

for number in set_of_numbers:
    print(number)