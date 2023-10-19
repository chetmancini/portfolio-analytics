from typing import Dict

from src.lookups.openai import AllocationAPIResponse


class AllocationLookupService:

    def __init__(self):
        self.cache: Dict[str, AllocationAPIResponse] = {}

    def get_allocations_by_symbol(self, symbol: str) -> AllocationAPIResponse:
        if symbol in self.cache:
            return self.cache[symbol]

        response = AllocationAPIResponse(symbol=symbol)
        self.cache[symbol] = response
        return response
