# try:
#     f = open('siple.txt', 'r')
#     f.write("Test write to simple text!")
# except IOError:
#     print("ERROR: could not find file or read data!")
# else:
#     print("SUCCESS!")
#     f.close()

try:
    f = open('basic/simple.txt', 'r')
    f.write("Test write to simple text!")
except:
    print("ERROR: could not find file or read data!")
finally:
    print("i always work no matter what")
