from enum import Enum


class CoreEnum(Enum):
    @classmethod
    def as_tuples(cls):
        return [(i.value, i.name) for i in cls]
