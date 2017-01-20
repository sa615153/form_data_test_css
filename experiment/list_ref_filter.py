# -*- coding: utf-8 -*-
class O(object):
    data = 0
    def __init__(self,d):
        self.data = d

e1 = O(1)
e2 = O(2)
print e1.data
print e2.data
e3 = O(3)
e4 = O(4)
e5 = O(5)
e6 = O(6)
e7 = O(7)
e8 = O(8)

l = [e1,e2,e3,e4,e5,e6,e7,e8]
e1.data = 0
print e1.data
print "---------------"
for e in l:
    print e.data

print "filter"

one_five = filter(lambda x:True if x.data < 6 else False,l)
for e in one_five:
    print e.data

print "two-----------"
two = filter(lambda x:True if x.data == 2 else False,l)
print two[0].data

print "two[0].data=new"
two[0].data="new"

for e in one_five:
    print e.data

print "filter出来的two[0].data改后，filter出来的one_five相应值也相应值也会改"