import json
from typing import Any
from dataclasses import dataclass


@dataclass
class DbModel:
    host_name: str
    port: str
    username: str
    password: str
    database: str
    table_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'DbModel':
        _host_name = str(obj.get("host_name"))
        _port = str(obj.get("port"))
        _username = str(obj.get("username"))
        _password = str(obj.get("password"))
        _database = str(obj.get("database"))
        _table_name = str(obj.get("table_name"))
        return DbModel(_host_name, _port, _username, _password, _database, _table_name)

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
