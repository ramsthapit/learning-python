# functions
def my_func(param1='default'):
    """documentation section"""
    print("my first python function {}".format(param1))


my_func()


def add(a, b):
    print(a+b)


add(1, 2)


def hello():
    return "hello"


result = hello()
print(result)


def addNum(num1, num2):
    if type(num1) == type(num2) == type(1):
        return num1+num2
    else:
        return " Sorry, i need integer"


result = addNum(2, 3)
print(result)
# print(result("e", "r"))


# # Lambda expression

# filter
mylist = [1, 2, 3, 4, 5, 6]


# def even_bool(num):
#     return num % 2 == 0


# evens = filter(even_bool, mylist)

evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))
print(evens)
