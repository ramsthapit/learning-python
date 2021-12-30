# Given a list of integers, return True if the sequence of numbers 1,2,3
# appears in the list somewhere.
# for eg:
# arrayCheck([1, 2, 3, 1]) - -True
# arrayCheck([1, 2, 1, 2, 3, 1]) - -True
# arrayCheck([1, 2, 1, 3, 1]) - -True


def arrayCheck(nums):

    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True

    return False


a = arrayCheck([1, 1, 12, 1, 2, 3, 4])
print(a)

# Given a string return a new string made of every other character starting
# with the first , so "Hello" yields "Hlo"


def stringBits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    print(result)


stringBits('hello')


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]


c = end_other("ram", "am")
print(c)

# given string and return double char


def doubleChar(str):
    result = ""
    for chr in str:
        result += chr * 2
    print(result)


doubleChar("ramsthapit")

# """no teen"""


def teen(a):
    if a > 12 and a < 20:
        return True


def no_teen_sum(a, b, c):
    if teen(a):
        a = 0
    if teen(b):
        b = 0
    if teen(c):
        c = 0
    print(a+b+c)


no_teen_sum(1, 12, 13)


def teen(a):
    if a > 12 and a < 20:
        return 0
    return a


def no_teen_sum(a, b, c):
    print(teen(a)+teen(b)+teen(c))


no_teen_sum(1, 12, 13)
