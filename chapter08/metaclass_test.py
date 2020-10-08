# -*- coding: utf-8 -*-

# 类也是对象，type实例化的对象


def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return 'user'

        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'

        return Company
    else:
        raise ValueError(f'Has no class called {name}.')


def user_init(self, name):
    self.name = name


class BaseUser:
    def say(self):
        print('saying...')


# type动态创建类
User = type('User', (BaseUser,), {'name': 'sss', '__init__': user_init})

# 元类是创建类的类  对象 <- class <- type


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class UserNew(metaclass=MetaClass):
    pass


if __name__ == '__main__':
    MyClass = create_class('user')
    my_obj = MyClass()
    print(my_obj)
    print(type(my_obj))
    obj2 = User(name='qqq')
    print(obj2.name)
    print(User.name)
    print(type(obj2))
    print(User.__dict__)
    print(obj2.__dict__)
    obj2.say()
    my_obj = UserNew()
    print(type(my_obj))
