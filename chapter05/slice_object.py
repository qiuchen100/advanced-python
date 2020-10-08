# -*- coding: utf-8 -*-

class Group:
    #支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self.group_name, self.company_name, staffs[item])
        elif isinstance(item, int):
            return cls(self.group_name, self.company_name, staffs[item:item+1])
        else:
            raise TypeError('item must be int or slice!')
        return self.staffs[item]

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        pass

    def __contains__(self, item):
        if item in self.staffs:
            return True
        return False

    def __str__(self):
        return f'Group : {self.group_name}, Company : {self.company_name} \n' \
               f'staffs : {",".join(self.staffs)}'

staffs = ['qq1', 'qq2', 'qq3', 'qq4', 'qq5']
group = Group(company_name='chite', group_name='user', staffs=staffs)
print(group)
print(group[1:2])
sub_group = group[:2]
print(sub_group)
print(group[2])
print('qq4' in group)
reversed(group)
print(group)