# looping over a collection/list


# C, for i = 0; i < n; i++

# lookup the ith word

# going to python, it's exactly the same thing

# In C
for i in xrange(len(text)):
    print text[i]

# In Python it's faster to
for word in text:
    print word
# simpler, easier to read, better and faster


# in C
for i in xrange(len(text)):
    print i, '-->', text[i]

performance
for count in xrange(2000):
    with open('sample.txt', 'w') as f:
        for i in xrange(len(text)):
            line = '{0} --> {1}'.format(i, text[i])
            f.write(line)
844004 function calls in 0.902 seconds

# # if manipulating indicies directly, it's probably wrong

# In Python
for i, word in enumerate(text):
    print i, '-->', word
# fast, beautiful, saves you from tracking individual indicies

for count in xrange(2000):
    with open('sample.txt', 'w') as f:
        for i, word in enumerate(text):
            line = '{0} --> {1}'.format(i, word)
            f.write(line)
#  842004 function calls in 0.873 seconds
