# -*- coding: utf-8 -*-

l = ['a', 'b', 'c', [1, 2, 3]]
import copy
a = copy.copy(l)
b = copy.deepcopy(l)
a.append('e')
b.append('f')
print(a, b, l)
a[3][2] = 'x'
b[3][2] = 'y'
print(a, b, l)

print "可见，浅拷贝后，父对象中的子对象，即上例中列表中的列表，还是被共享着的；"

print "\n\n\n"



def foo(x, y):
    print x, y

alist = [1, 2]
adict = {'x': 1, 'y': 2}

foo(*alist)  # 1, 2

foo(**adict)  # 1, 2



print "Hello %(name)s !" % {'name': 'James'}
# Hello James !
print "I am years %(age)i years old" % {'age': 18}
# I am years 18 years old


print "\n\n\n"

l = [(i, j) for i in range(4) for j in range(i)]
print l

print range(3)



# a, b, *rest = range(10)



n = 16
myDict = {}
for i in range(0, n):
    char = 'abcd'[i%4]
    if char not in myDict:
        myDict[char] = 0
        myDict[char] += 1
    else:
        myDict[char] += 1
        print(myDict)

print "--------------"
n = 16
myDict = {}
for i in range(0, n):
    char = 'abcd'[i%4]
    try:
        myDict[char] += 1
    except KeyError:
        myDict[char] = 1
    print(myDict)

print "----------"
print  'abcd'[2]

print "\n\n\n"

import os
# def tree(top):
#     for path, names, fnames in os.walk(top):
#         for fname in fnames:
#             yield os.path.join(path, fname)
#
# for name in tree('C:\Users\jpang3\Downloads'):
#     print name



t = os.walk('C:\Users\jpang3\Downloads')
print t
print type(t)

lt = list(t)
print lt


print "\n\n\n"

#iter and generator
#the first try
#=================================
i = iter('abcd')
print i.next()
print i.next()
print i.next()

s = {'one':1,'two':2,'three':3}
print s
m = iter(s)
print m.next()
print m.next()
print m.next()

print "----------------------------"
a = [1, 2, 3]
b = ['a', 'b', 'c']
print zip(a, b)
print "unzip"
z = zip(a, b)
print zip(*z)

print "----------------------------"
a = [1, 2, 3, 4, 5, 6]

print a*3

print iter(a)
print [iter(a)]
print [iter(a)]*3
print ([iter(a)]*3)

print zip(*([iter(a)]*3))  # three iterators
print zip(*([iter(a)]*2))  # two iterators
