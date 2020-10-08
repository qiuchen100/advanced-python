# -*- coding: utf-8 -*-
class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year}/{self.month}/{self.day}'

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_date_str(date_str):
        year, month, day = date_str.split('-')
        date = Date(int(year), int(month), int(day))
        return date

    @classmethod
    def from_str(cls, date_str):
        year, month, day = date_str.split('-')
        date = cls(int(year), int(month), int(day))
        return date


if __name__ == '__main__':
    date = Date(2009, 12, 1)
    date.tomorrow()
    print(date)
    date_str = '2018-12-31'
    new_day = Date.parse_date_str(date_str)
    print(new_day)
    new_day2 = Date.from_str(date_str)
    print(new_day)