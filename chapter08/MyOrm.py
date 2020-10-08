# -*- coding: utf-8 -*-
import numbers


class Field:
    pass


class IntField(Field):
    def __init__(self, db_column, min_value=None, max_value=None):
        min_value = 0 if min_value is None else min_value
        max_value = float('inf') if max_value is None else max_value
        if min_value is not None and not isinstance(
                min_value, numbers.Integral):
            raise ValueError('min_value must be int')
        if max_value is not None and not isinstance(
                max_value, numbers.Integral):
            raise ValueError('max_value must be int')
        if min_value < 0:
            raise ValueError('min_value must be positive')
        if max_value < 0:
            raise ValueError('max_value must be positive')
        if min_value > max_value:
            raise ValueError('min_value can not bigger than max_value')
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('Int value need!')
        if not self.min_value <= value <= self.max_value:
            raise ValueError('Value must between min_value and max_value!')
        self._value = value


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        if max_length is not None and max_length <= 0:
            raise ValueError('Positive value need!')
        self.max_length = max_length if max_length is not None else float(
            'inf')
        self.db_column = db_column
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('str value need!')
        if len(value) > self.max_length:
            raise ValueError('over max length!')
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'db_table', None)
            if table is not None:
                db_table = table
        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()


class User(BaseModel):
    name = CharField(db_column='nm', max_length=20)
    age = IntField(db_column='', max_value=100)

    class Meta:
        db_table = 'user'

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column if value.db_column else key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))
        db_table = self._meta['db_table']
        sql = f'insert into {db_table} ({",".join(fields)}) ' \
              f'values ({",".join(values)});'
        print(sql)

    def __str__(self):
        return f'Name : {self.name}, Age : {int(self.age)}'


if __name__ == '__main__':
    user = User()
    user.name = 'qq'
    user.age = 12
    # print(user)
    user.save()
