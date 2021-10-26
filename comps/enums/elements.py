from core.enums import CoreEnum

class ElementEnum(CoreEnum):
    WIND = 1
    WATER = 2
    FLAME = 3
    LIGHT = 4
    SHADOW = 5

    def get_name(self):
        return '{}',format(self.name)