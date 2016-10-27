print type.__call__
print type.__doc__
print "---------------------"
cls = type('A', (object,), {})
print cls.__name__
print cls.__doc__
print cls.__module__
print sorted(cls.__dict__.keys())
