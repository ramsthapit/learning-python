# Lists
mylist = [1, 2, 3]
print(mylist)  # [1, 2, 3]

list = ['ram', 2, 3, [1, 2, 3]]
print(list)  # ['ram', 2, 3, [1, 2, 3]]

print(mylist[0])

# slicing on list

a = ['a', 'b', 'c', 'd', 'e']
print(a)
print(a[:1])  # a
print(a[::2])  # ['a', 'c', 'e']
print(a[2])  # c
print(a[:2:])  # ['a', 'b']
print(a[1:])  # ['b', 'c', 'd', 'e']
print(a[:4])  # ['a', 'b', 'c', 'd']

# Update item in list
a[0] = 'Ram'
print(a)  # ['Ram', 'b', 'c', 'd', 'e']

# Append on list
a.append('alist00')
print(a)  # ['Ram', 'b', 'c', 'd', 'e', 'alist00']

a = ['a', 'b', 'c', 'd', 'e']
b = ['x', 'y', 'z']

# a.append(b)
# print(a)  # ['a', 'b', 'c', 'd', 'e', ['x', 'y', 'z']]

# # Extend a list
# a.extend(b)
# print(a)  # ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']

# # Remove from list
# c = a.pop()
# print(c)
# print(a)

# Reverse a list
a.reverse()
print(a)  # ['e', 'd', 'c', 'b', 'a']

# Sort a list
z = [9, 5, 3, 8, 2]
z.sort()
print(z)

# nested list
list = [1, 2, ['w', 'y', 'r']]
print(list)

# comprehensive list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)
