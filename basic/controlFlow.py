# # if else statement

# if 1 > 2:
#     print('yes!')
# elif 3 == 3:
#     print('3')
# else:
#     print('last')


# # For loops
# seq = [1, 2, 3, 4, 5, 6]

# for items in seq:
#     print(items)
#     print('hello')

# d = {'sam': 1, "Frank": 2, "Dan": 3}

# for k in d:
#     print(k)
#     print(d[k])


# # Tuples

# mypairs = [(1, 2), (3, 4)]
# for items in mypairs:
#     print(items)
# for tup1, tup2 in mypairs:
#     print(tup2)
#     print(tup1)


# # # while loop
# i = 1
# while i < 5:
#     print("i is: {}".format(i))
#     i = i+1


# # range function
# for item in range(10):
#     print(item)

# list comprehension
x = [1, 2, 3, 4]
out = []
# for num in x:
#     out.append(num**2)
# print(out)

out = [num**2 for num in x]
print(out)
