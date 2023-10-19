from enum import Enum


class RegionType(Enum):
    US = 1
    INTERNATIONAL = 2


class AllocationStyle(Enum):
    GROWTH = 1
    VALUE = 2
    BLEND = 3
    UNKNOWN = 4


class GeographicalRegion(Enum):
    NORTH_AMERICA = "North America"
    EMEA = "Europe, Middle East, and Africa"
    LATAM = "Latin America"
    APAC = "Asia-Pacific"
    GLOBAL = "Global"


class EconomicStatus(Enum):
    DEVELOPED = "Developed Markets"
    EMERGING = "Emerging Markets"
    FRONTIER = "Frontier Markets"


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

    economic_status = {
        EconomicStatus.DEVELOPED: 100,
        EconomicStatus.EMERGING: 0,
        EconomicStatus.FRONTIER: 0,
    }

    geographic_region = {
        GeographicalRegion.NORTH_AMERICA: 0,
        GeographicalRegion.EMEA: 0,
        GeographicalRegion.LATAM: 0,
        GeographicalRegion.APAC: 0,
        GeographicalRegion.GLOBAL: 100,
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

    def set_economic_status(self, economic_status: EconomicStatus):
        if economic_status not in EconomicStatus:
            raise ValueError('Invalid economic status')
        if economic_status == EconomicStatus.DEVELOPED:
            self.economic_status = {
                EconomicStatus.DEVELOPED: 100,
                EconomicStatus.EMERGING: 0,
                EconomicStatus.FRONTIER: 0,
            }
        elif economic_status == EconomicStatus.EMERGING:
            self.economic_status = {
                EconomicStatus.DEVELOPED: 0,
                EconomicStatus.EMERGING: 100,
                EconomicStatus.FRONTIER: 0,
            }
        elif economic_status == EconomicStatus.FRONTIER:
            self.economic_status = {
                EconomicStatus.DEVELOPED: 0,
                EconomicStatus.EMERGING: 0,
                EconomicStatus.FRONTIER: 100,
            }
        else:
            raise ValueError('Invalid economic status')

    def set_economic_status_values(self, developed: int = 0, emerging: int = 0, frontier: int = 0):
        self.economic_status = {
            EconomicStatus.DEVELOPED: developed,
            EconomicStatus.EMERGING: emerging,
            EconomicStatus.FRONTIER: frontier,
        }

    def set_geographic_region(self, geographic_region: GeographicalRegion):
        if geographic_region not in GeographicalRegion:
            raise ValueError('Invalid geographic region')
        if geographic_region == GeographicalRegion.GLOBAL:
            self.geographic_region = {
                GeographicalRegion.NORTH_AMERICA: 0,
                GeographicalRegion.EMEA: 0,
                GeographicalRegion.LATAM: 0,
                GeographicalRegion.APAC: 0,
                GeographicalRegion.GLOBAL: 100,
            }
        else:
            self.geographic_region = {
                GeographicalRegion.NORTH_AMERICA: 100 if geographic_region == GeographicalRegion.NORTH_AMERICA else 0,
                GeographicalRegion.EMEA: 100 if geographic_region == GeographicalRegion.EMEA else 0,
                GeographicalRegion.LATAM: 100 if geographic_region == GeographicalRegion.LATAM else 0,
                GeographicalRegion.APAC: 100 if geographic_region == GeographicalRegion.APAC else 0,
                GeographicalRegion.GLOBAL: 0,
            }

    def set_geographic_region_values(self, north_america: int = 0, emea: int = 0, latam: int = 0, apac: int = 0,
                                     global_: int = 0):
        self.geographic_region = {
            GeographicalRegion.NORTH_AMERICA: north_america,
            GeographicalRegion.EMEA: emea,
            GeographicalRegion.LATAM: latam,
            GeographicalRegion.APAC: apac,
            GeographicalRegion.GLOBAL: global_,
        }

    def validate(self):
        if sum(self.us_international.values()) != 100:
            raise ValueError('US and International must sum to 100')
        if sum(self.allocation_style.values()) != 100:
            raise ValueError('Allocation style must sum to 100.')
        if sum(self.economic_status.values()) != 100:
            raise ValueError('Economic status must sum to 100.')
        if sum(self.geographic_region.values()) != 100:
            raise ValueError('Geographic region must sum to 100.')
