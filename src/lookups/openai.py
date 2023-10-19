import os

import openai

from typing import Optional
from pydantic import BaseModel


class USInternationalAllocation(BaseModel):
    us: int
    international: int


class RegionAllocation(BaseModel):
    north_america: int
    eama: int
    latam: int
    apac: int
    global_: int


class FundAssetAllocation(BaseModel):
    stocks: int
    bonds: int
    real_estate: int
    cash: int


class MarketCapAllocation(BaseModel):
    large_cap: int
    mid_cap: int
    small_cap: int


class GrowthValueAllocation(BaseModel):
    growth: int
    value: int


class EconomicStatusAllocation(BaseModel):
    developed: int
    emerging: int
    frontier: int


class AllocationAIResponse(BaseModel):
    symbol: str
    security_name: str

    fund_asset_allocation: FundAssetAllocation
    market_cap_allocation: MarketCapAllocation
    us_international_allocation: USInternationalAllocation
    region_allocation: RegionAllocation
    growth_value_allocation: GrowthValueAllocation
    economic_status_allocation: EconomicStatusAllocation


class OpenAIClient:

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def lookup_allocation(self, symbol: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user",
                 "content": f"Give me an asset allocation breakdown for {symbol}. "
                            f"Give data as an integer percentage for the funds assets (stocks vs bonds), "
                            f"the market cap, usa vs international, and growth vs value. "
                            f"If it's a blend use 50-50 for growth / value."}
            ],
            functions=[
                {
                    "name": "get_answer_for_user_query",
                    "description": "Get user answer in series of steps. "
                                   "First the name, "
                                   "then the fund asset allocation percentage of stocks and bonds (if it is a fund), "
                                   "then the market cap weighting, "
                                   "then percent us and international, then if it's growth or value, "
                                   "and finally the economic status breakdown of the portfolio's holdings "
                                   "(developed, emerging, or frontier)",
                    "parameters": AllocationAIResponse.schema()
                }
            ],
            function_call={"name": "get_answer_for_user_query"}
        )
        return AllocationAIResponse.model_validate_json(response.choices[0]["message"]["function_call"]["arguments"])
