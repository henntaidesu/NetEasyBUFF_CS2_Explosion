from typing import Any
from dataclasses import dataclass
import json


@dataclass
class SteamItem:
    item_name: str
    game_name: str
    shelf_date: str
    transaction_date: str
    trading_partners: str
    price: float

    @staticmethod
    def from_dict(obj: Any) -> 'SteamItem':
        _item_name = str(obj.get("item_name"))
        _game_name = str(obj.get("game_name"))
        _shelf_date = str(obj.get("_shelf_date"))
        _transaction_date = str(obj.get("transaction_date"))
        _trading_partners = str(obj.get("trading_partners"))
        _price = float(obj.get("price"))

        return SteamItem(_item_name, _game_name, _shelf_date, _transaction_date, _trading_partners, _price)

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
