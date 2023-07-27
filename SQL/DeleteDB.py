import pymysql
from Function.OpenJson import read_database_config

class DeleteDB:

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

    def delete_buy_item(self) -> bool:
        cursor = self.db.cursor()
        try:
            sql = f"DELETE FROM {self.table_name}"
            cursor.execute(sql)
            self.db.commit()
            cursor.close()
            return True
        except:
            return False

    def delete_sell_item(self) -> bool:
        cursor = self.db.cursor()
        try:
            sql = f"DELETE FROM {self.sell_table_name}"
            cursor.execute(sql)
            self.db.commit()
            cursor.close()
            return True
        except:
            return False

    def delete_buy_order_time_limit1(self, ordertime) ->bool:
        curses = self.db.cursor()
        try:
            sql = f"DELETE FROM {self.table_name} WHERE order_time >='{ordertime}'"
            curses.execute(sql)
            self.db.commit()
            curses.close()
            return True
        except:
            return False


    def delete_buy_sell_time_limit1(self, ordertime) ->bool:
        curses = self.db.cursor()
        try:
            sql = f"DELETE FROM {self.sell_table_name} WHERE order_time >='{ordertime}'"
            curses.execute(sql)
            self.db.commit()
            curses.close()
            return True
        except:
            return False





