from my_set import MySet

set_of_errors = MySet()
set_of_errors.add([1, 2]) # This will likely cause an error because lists are not hashable
set_of_errors.add((2, 3, 2))
set_of_errors.add((1, 3))

for error in set_of_errors:
    print(error)