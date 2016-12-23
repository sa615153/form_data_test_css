import pystache

class T(object):
    def __init__(self,track_number = 'none',subtasks='subs',):
        self.track_number = 1
        self.subtasks=2

task = T()

print pystache.render('Hi {{task.subtasks}}!', {'task': task})
str = 'http://hao.jobbole.com/pystache/'