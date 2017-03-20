import abc


ATTRIBUTES = ['str', 'int', 'dex', 'wis', 'con', 'cha']


class Person(metaclass=abc.ABCMeta):
    def __init__(self, level, attributes):
        self.level = level
        self.attributes = {ATTRIBUTES[i]: attributes[i] for i in range(len(attributes))}

    def modifier(self, attr_score):
        return int((attr_score - 8) / 4)

