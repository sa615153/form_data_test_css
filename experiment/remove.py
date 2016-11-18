class A(object):

    def __init__(self,i):
        self.a = i


a1 = A(1)
a2 = A(2)
a3 = A(3)
a4 = A(4)
a5 = A(5)


list1 = [a1,a2,a3,a4,a5]

print "list1"
for i in list1:
    print i
    print i.a

list2 = filter(lambda x:True if x.a<3 else False,list1)
print "*********************after filter list2****************************"
for i in list2:
    print i
    print i.a



print "******************"
list1.remove(list2[0])

print "***************list1:  after remove list2[0] from list1:********************"
for i in list1:
    print i
    print i.a


print "***************list2:  after remove list2[0] from list1:********************"
for i in list2:
    print i
    print i.a


# list2[0]===list1[0]===address