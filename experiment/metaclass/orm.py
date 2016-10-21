# -*- coding: utf-8 -*-
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)



class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name  # 假设表名和类名一致
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))  # 后改的ｉｄ值在这个时候被读取#################################
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))          #
        print('SQL: %s' % sql)                                                                                  #
        print('ARGS: %s' % str(args))                                                                           #
                                                                                                                #
class User(Model):                                                                                             #
    # 定义类的属性到列的映射：                                                                                  #
    id = IntegerField('id')                                                                                     #
    name = StringField('username')                                                                              #
    email = StringField('email')                                                                                #
    password = StringField('password')                                                                          #
                                                                                                                #
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')                                     #
u.id = 1  # #################################################################################################?
u.save()

# name = stringfield
# 注意不是ｓｔｒｉｎｇ　ｎａｍｅ　＝　张三，这不是普通的成员变量声明，而是制定类型，将类型在某处存下来