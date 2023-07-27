from typing import Any
from dataclasses import dataclass
import json

@dataclass
class SellItem:
    weapon_name: str
    item_name: str
    weapon_float: float
    float_range: str
    price: int
    bargain_price: int
    buyer_name: str
    order_time: str
    status: str

    def __init__(self):
        self.temp_time = None
        self.seller_name = None

    @staticmethod
    def from_dict(obj: Any) -> 'SellItem':
        _weapon_name = str(obj.get("weapon_name"))
        _item_name = str(obj.get("item_name"))
        _weapon_float = float(obj.get("weapon_float"))
        _float_range = str(obj.get("float_range"))
        _price = int(obj.get("price"))
        _bargain_price = int(obj.get("bargain_price"))
        _buyer_name = str(obj.get("seller_name"))
        _order_time = str(obj.get("order_time"))
        _status = str(obj.get("status"))

        return SellItem(_weapon_name, _item_name, _weapon_float, _float_range, _price, _bargain_price,
                        _buyer_name, _order_time, _status)

    def to_json(self) -> str:
        return json.dumps(self.__dict__)