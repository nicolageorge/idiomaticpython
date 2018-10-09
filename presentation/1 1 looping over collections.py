# looping over a collection/list
# text = ['red', 'green', 'blue', 'yellow']
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
          quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
          Cras tristique quis est accumsan molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc auctor, massa et faucibus auctor, 
          lorem turpis finibus enim, et fringilla nisi nisl vel felis. Fusce commodo pretium semper. Phasellus eget enim non mi ullamcorper imperdiet non ut 
          nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam dignissim hendrerit tempus. Nam volutpat lorem ac dui vulputate, vitae facilisis
          mi accumsan. Pellentesque aliquam risus tellus, eu tincidunt elit laoreet ut. Curabitur facilisis ac purus sed vulputate."""


text = text.replace(',', '').split(' ')
# print text

# C, for i = 0; i < n; i++

# lookup the ith word
# going to python, it's exactly the same thing

# In C
# for i in xrange(len(text)):
#     print text[i]


# for i in xrange(1000):
#     with open('sample.txt', 'w') as f:
#         for i in xrange(len(text)):
#             f.write(text[i])
# 72004 function calls in 0.230 seconds,
# len function called 1000 times


# In Python it's faster to
# for word in text:
#   print word

# performance
# for i in xrange(1000):
#     with open('sample.txt', 'w') as f:
#         for word in text:
#             f.write(word)
# 70004 function calls in 0.209 seconds


# # looping backwards
# In C
# for i in xrange(len(text)-1, -1, -1):
#     print text[i]

# performance
# for count in xrange(1000):
#     with open('sample.txt', 'w') as f:
#         for i in xrange(len(text)-1, -1, -1):
#             f.write(text[i])
# 72005 function calls in 0.214 seconds
# len called 1000 times

# In Python
# for word in reversed(text):
#   print word

# performance
# for count in xrange(1000):
#     with open('sample.txt', 'w') as f:
#         for word in reversed(text):
#             f.write(word)
# 70004 function calls in 0.206 second

# looping over a collection and indicies

# in C
# for i in xrange(len(text)):
#    print i, '-->', text[i]

# performance
# for count in xrange(2000):
#     with open('sample.txt', 'w') as f:
#         for i in xrange(len(text)):
#             line = '{0} --> {1}'.format(i, text[i])
#             f.write(line)
# 844004 function calls in 0.902 seconds

# # if manipulating indicies directly, it's probably wrong

# In Python

# for i, word in enumerate(text):
#     print i, '-->', word

# for count in xrange(2000):
#     with open('sample.txt', 'w') as f:
#         for i, word in enumerate(text):
#             line = '{0} --> {1}'.format(i, word)
#             f.write(line)
#  842004 function calls in 0.873 seconds



