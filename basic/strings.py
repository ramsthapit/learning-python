# a =2
# print(a*20)

a = 'ramsthapit'
# print(a[:2])  # ra
# print(a[::2])  # rmtai
# print(a[::-1])  # tipahtsmar
# print(a)

# Uppercase
x = a.upper()
print(x)  # RAMSTHAPIT

# Lowercase
x = x.lower()
print(x)  # ramsthapit

# Capitalize
x = x.capitalize()
print(x)  # Ramsthapit

b = 'ram sthapit'

# split word

x = b.split()
print(x)  # ['ram', 'sthapit']

x = b.split('a')
print(x)  # ['r', 'm sth', 'pit']

# Print formatting
x = "insert another string here: {}".format("Insert me")
print(x)  # insert another string here: Insert me

z = "Item one: {}, Item two: {}".format("dog", "cat")
print(z)  # Item one: dog, Item two: cat

z = "Item one: {c}, Item two: {d}".format(d="dog", c="cat")
print(z)  # Item one: cat, Item two: dog
