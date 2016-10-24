#!/usr/bin/python
# coding :utf-8

def monkey_patch(name, bases, dct):
    assert len(bases) == 1
    base = bases[0]
    for name, value in dct.iteritems():
        if name not in ('__module__', '__metaclass__'):
            setattr(base, name, value)
    return base


class A(object):
    def a(self):
        print 'i am A object'


class PatchA(A):
    __metaclass__ = monkey_patch

    def patcha_method(self):
        print 'this is a method patched for class A'


def main():
    pa = PatchA()
    pa.patcha_method()
    pa.a()
    print dir(pa)
    print dir(PatchA)


if __name__ == '__main__':
    main()