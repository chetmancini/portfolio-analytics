import pytest

from src.portfolio.allocation import SecurityAllocation, AllocationStyle, RegionType


class TestSecurityAllocation:

    def test_set_allocation_style(self):
        allocation = SecurityAllocation()
        allocation.set_allocation_style(AllocationStyle.GROWTH)
        assert allocation.allocation_style == {
            AllocationStyle.GROWTH: 100,
            AllocationStyle.VALUE: 0,
            AllocationStyle.UNKNOWN: 0,
        }

        allocation.set_allocation_style(AllocationStyle.VALUE)
        assert allocation.allocation_style == {
            AllocationStyle.GROWTH: 0,
            AllocationStyle.VALUE: 100,
            AllocationStyle.UNKNOWN: 0,
        }

        allocation.set_allocation_style(AllocationStyle.BLEND)
        assert allocation.allocation_style == {
            AllocationStyle.GROWTH: 50,
            AllocationStyle.VALUE: 50,
            AllocationStyle.UNKNOWN: 0,
        }

    def test_set_us_international(self):
        allocation = SecurityAllocation()
        allocation.set_us_international(us=40, international=60)
        assert allocation.us_international == {
            RegionType.US: 40,
            RegionType.INTERNATIONAL: 60,
        }

    def test_validate(self):
        allocation = SecurityAllocation()
        allocation.set_us_international(us=40, international=60)
        allocation.validate()

    def test_validate_invalid(self):
        allocation = SecurityAllocation()
        with pytest.raises(ValueError):
            allocation.validate()

    def test_validate_invalid_sum(self):
        allocation = SecurityAllocation()
        allocation.set_us_international(us=40, international=50)
        with pytest.raises(ValueError):
            allocation.validate()
