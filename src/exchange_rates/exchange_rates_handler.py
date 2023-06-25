from dataclasses import dataclass, field
from functools import lru_cache
from src import client_session


@dataclass
class ExchangeRatesHandler:
    exchange_rates: dict = field(default_factory=dict)
    
    @classmethod
    @lru_cache
    async def get_exchange_rates(cls):
        api_url = "https://www.cbr-xml-daily.ru/latest.js"
        async with client_session.get(api_url) as resp:
            if resp.status_code == 200:
                cls.exchange_rates = await resp.json()
            else:
                print("Error:", resp.status_code, resp.text)

    @classmethod
    @property
    @lru_cache
    def usd(cls):
        return cls.exchange_rates.get("rates", {}).get("usd")
