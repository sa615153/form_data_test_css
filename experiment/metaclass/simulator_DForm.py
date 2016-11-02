class FlatMetaClass(type):
    def __new__(cls,name,bases,attrs):
        wait = {}
        for aname, avalue in attrs.iteritems():
            if aname == "subdict":  # value is a dict{checkgui:checkbox}
                wait.update(avalue)
        print attrs
        attrs.pop('subdict')
        print attrs
        attrs.update(wait)
        return type.__new__(cls, name, bases, attrs)


class form(object):
    __metaclass__ = FlatMetaClass
    normal1 = "123"
    normal2 = 1
    subdict = {"checkgui": "obj", "compile": "obj2"}


def main():
    t = form()
    print dir(t)
    print t.checkgui
    print "vars"
    print vars(t)

if __name__ == '__main__':
    main()