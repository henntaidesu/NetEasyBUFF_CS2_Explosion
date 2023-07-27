import pymysql
import time
from Function.OpenJson import read_database_config


# from Function import GetMainInsertDB


class UpdateDB:

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

    def get_update_buy(self):
        cursor = self.db.cursor()
        # print(sql)
        try:
            sql = f"SELECT COUNT(*) , MIN(order_time) FROM BuffBuyHistory WHERE " \
                  f"status LIKE '%等待%' OR status LIKE '%正在%' OR status LIKE '%交易%' " \
                  f"OR status LIKE '%报价失败%' OR status = '结算中'"
            cursor.execute(sql)
            results = cursor.fetchall()
            data = results[0]
            # +print(data[1])
            print("共删除数据：", data[0], "条")
            sql = f"DELETE FROM  {self.table_name} WHERE order_time >= '{data[1]}'"
            # print(sql)
            cursor.execute(sql)
            print("请执行1进行更新数据")
            time.sleep(2)
            self.db.commit()
        except IndexError as e:
            print(f"\n无匹配数据: {e} \n")
        cursor.close()
