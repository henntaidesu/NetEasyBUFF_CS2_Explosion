import pymysql
from datetime import datetime
from Model.HistoryItem import HistoryItem
from Model.SellItem import SellItem
from Model.SteamItem import SteamItem
from Function.OpenJson import read_database_config

class InsterDB:

    def __init__(self, table_name: str = 'BuffBuyHistory', sell_table_name: str = 'BuffSellRecord',
                 steam_record: str = 'SteamRecord', funds: str = 'funds'):
        self.sale_table_name = None
        host, port, user, password, database = read_database_config()
        self.db = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=password,
                                  database=database)
        self.table_name = table_name
        self.funds = funds
        self.sell_table_name = sell_table_name
        self.steam_record = steam_record

    def insert_buff_buy_item(self, item: HistoryItem, ordertime) -> bool:
        temp_time = item.order_time
        temp_time = datetime.strptime(temp_time, '%Y-%m-%d %H:%M:%S')
        if ordertime <= temp_time:
            cursor = self.db.cursor()
            storage_time = datetime.now()
            item.item_name = item.item_name.replace("'", "\\'")
            item.weapon_name = item.weapon_name.replace("'", "\\'")
            sql = f"insert into {self.table_name} (`weapon_name`, `item_name`, `weapon_float`, " \
                  f"`float_range`, `price`, `bargain_price`, `seller_name`, `order_time`, `status`, `storage_time`) " \
                  f" values ('{item.weapon_name}'," \
                  f"'{item.item_name}', {item.weapon_float}, '{item.float_range}'," \
                  f"{item.price}, {item.bargain_price}, '{item.seller_name}'," \
                  f"'{item.order_time}', '{item.status}', '{storage_time}')"
            # print(sql)
            try:
                cursor.execute(sql)
                self.db.commit()
                cursor.close()
                return True
            except Exception as e:
                print(e)
                cursor.close()
                return False
        else:
            print("无新数据")
            return False

    def insert_buff_sell_item(self, item: SellItem, ordertime) -> bool:
        temp_time = item.order_time
        temp_time = datetime.strptime(temp_time, '%Y-%m-%d %H:%M:%S')
        if ordertime < temp_time:
            cursor = self.db.cursor()
            storage_time = datetime.now()
            item.item_name = item.item_name.replace("'", "\\'")
            item.weapon_name = item.weapon_name.replace("'", "\\'")
            sql = f"insert into `{self.sell_table_name}`(`weapon_name`, `item_name`, `weapon_float`," \
                  f"`float_range`, `price`, `bargain_price`, `buyer_name`, `order_time`, `status`,"\
                  f"`storage_time`) values " \
                  f"('{item.weapon_name}'," \
                  f"'{item.item_name}', {item.weapon_float}, '{item.float_range}'," \
                  f"{item.price}, {item.bargain_price}, '{item.seller_name}'," \
                  f"'{item.order_time}', '{item.status}', '{storage_time}')"
            # print(sql)
            try:
                cursor.execute(sql)
                self.db.commit()
                cursor.close()
                return True
            except Exception as e:
                print(e)
                cursor.close()
                return False
        else:
            print("无新数据")
            return False

    def insert_steam_item(self, item: SteamItem, ordertime) -> bool:
        temp_time = item.order_time
        temp_time = datetime.strptime(temp_time, '%Y-%m-%d')
        if ordertime < temp_time:
            cursor = self.db.cursor()
            storage_time = datetime.now()

    def insert_funds_item(self, sources_of_funds, type , amount, date):
        cursor = self.db.cursor()
        sql = f"INSERT INTO {self.funds}(`sources_of_funds`, `type`, `amount`, `date`) VALUES" \
              f" ('{sources_of_funds}', '{type}', {amount}, '{date}')"
        # print(sql)
        try:
            cursor.execute(sql)
            self.db.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            cursor.close()
        return False

