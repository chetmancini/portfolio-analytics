from enum import Enum


class RegionType(Enum):
    US = 1
    INTERNATIONAL = 2


class AllocationStyle(Enum):
    GROWTH = 1
    VALUE = 2
    BLEND = 3
    UNKNOWN = 4


class MarketCap(Enum):
    LARGE = 1
    MID = 2
    SMALL = 3


class SecurityAllocation:
    us_international = {
        RegionType.US: 0,
        RegionType.INTERNATIONAL: 0,
    }

    allocation_style = {
        AllocationStyle.GROWTH: 0,
        AllocationStyle.VALUE: 0,
        AllocationStyle.UNKNOWN: 100,
    }

    def set_allocation_style(self, allocation_style: AllocationStyle):
        if allocation_style not in AllocationStyle:
            raise ValueError('Invalid allocation style')
        if allocation_style == AllocationStyle.BLEND:
            self.allocation_style = {
                AllocationStyle.GROWTH: 50,
                AllocationStyle.VALUE: 50,
                AllocationStyle.UNKNOWN: 0,
            }
        else:
            self.allocation_style = {
                AllocationStyle.GROWTH: 100 if allocation_style == AllocationStyle.GROWTH else 0,
                AllocationStyle.VALUE: 100 if allocation_style == AllocationStyle.VALUE else 0,
                AllocationStyle.UNKNOWN: 100 if allocation_style == AllocationStyle.UNKNOWN else 0,
            }

    def set_us_international(self, us: int = 0, international: int = 0):
        self.us_international = {
            RegionType.US: us,
            RegionType.INTERNATIONAL: international,
        }

    def validate(self):
        if sum(self.us_international.values()) != 100:
            raise ValueError('US and International must sum to 100')
        if sum(self.allocation_style.values()) != 100:
            raise ValueError('Allocation style must sum to 100.')
