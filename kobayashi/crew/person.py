import abc


ATTRIBUTES = ['str', 'int', 'dex', 'wis', 'con', 'cha']


class Person(metaclass=abc.ABCMeta):
    def __init__(self, level, skill_mod):
        self.level = level
        self.skillmod = skill_mod
