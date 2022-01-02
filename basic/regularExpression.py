import re

# patterns = ['term1', 'term2']

# text = 'This is a string with term1, not the other'

# for pattern in patterns:
#     print("i'm searching for : "+pattern)
#     if re.search(pattern, text):
#         print("MATCH")
#     else:
#         print("NO MATCH")


text = 'This is a string with term1, not the other'
match = re.search('term1', text)
print(match.start())
print(type(match))


split_term = '@'

email = 'user@gmail.com'

match = re.split(split_term, email)
print(match)


match = re.findall('ram', 'ram sthapit is the name of ram. Ram stands for ')
print(match)


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')


# test_phrase = 'sdsd..ssdd.sdddddddddddd.s............sssdssss.ssdsdsdsdd'
# test_patterns = ['sd*']

# multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string! But is has punctuation.werw34 How can we 1234 remove it ?'

test_patterns = ['[A-Z]+']
# test_patterns = [r'\d+']
test_patterns = [r'\S+']
# test_patterns = [r'\s+']
multi_re_find(test_patterns, test_phrase)
