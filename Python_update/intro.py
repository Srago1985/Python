print('1')
print('2', end=' ')
print('3')


x = 10 #int
print('x =', x)
print (f"x = {x}")

y = 3.1415926 #float
print('pi =', y)
print(f"pi = {y}")

z = 'Hello' #str
print('z =', z)
print(f"z = {z}")

x = True #bool
print('x =', x)
print(f"x = {x}")

def check_army(age):
    return 18 <= age < 45

print(check_army(20))
print(check_army(50))

def barmen(age):
    volume = 42 if age >= 18 else 1.5
    return volume

list_of_ages = [15, 18, 20, 25, 30, 50]
for age in list_of_ages:
    print(f"Age: {age}, Barmen volume: {barmen(age)}")

print(len(list_of_ages))

number = 1655587745
print(len(str(number)))

def sum_of_list(lst):
    return sum(lst)

print(sum_of_list(list_of_ages))

lst = []
for i in range(10):
    lst.append(i)

lst = list(range(3, 12))