import pymysql
from datetime import datetime
from Function.OpenJson import read_database_config


class SelectDB:
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

    def is_select_bargain_price(self):
        cursor = self.db.cursor()
        sql = f"SELECT sum(bargain_price) FROM BuffBuyHistory WHERE `status` like '%成功%'"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            data = data[0]
            data = data[0]
            cursor.close()
            return float('%0.2f' % data)
        except:
            print("Err")
            cursor.close()
            return 1

    def is_select_sell_price(self):
        cursor = self.db.cursor()
        sql = f"SELECT sum(bargain_price) FROM BuffSellRecord WHERE `status` = '出售成功'"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            data = data[0]
            data = data[0]
            cursor.close()
            return float('%0.2f' % data)
        except:
            print("无数据，请执行1")
            cursor.close()
            return 1

    def is_select_bargain_wait(self):
        sql = f"SELECT COUNT(*) FROM {self.table_name} WHERE " \
              f"`status` like '等待%' or `status` like '正在%' or `status` like '%报价失败%' or `status` = '结算中'"
        # print(sql)
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            data = data[0]
            data = data[0]
            cursor.close()
            return data
        except:
            print("ERR")
            cursor.close()

    def is_get_bargain_list_all(self):
        cursor = self.db.cursor()
        sql = f"SELECT weapon_name, item_name, float_range,COUNT(`status`) FROM {self.table_name} " \
              f"WHERE `status` = '购买成功'" \
              f"GROUP BY weapon_name,item_name,float_range,`status` ORDER BY COUNT(`status`) DESC "
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            # print(data, "\n")
            for i in data:
                print(i)
            cursor.close()
        except:
            print("Err")
            cursor.close()

    def is_select_bargain_count(self, item_name):
        sql1 = f"SELECT AVG(bargain_price) FROM {self.table_name} WHERE item_name LIKE '%{item_name}%' " \
               f"and (status = '购买成功' OR status = '求购成功')"
        sql2 = f"SELECT COUNT(*) FROM {self.table_name} WHERE item_name LIKE '%{item_name}%' " \
               f"and  (status = '购买成功' OR status = '求购成功')"
        sql3 = f"SELECT price FROM {self.table_name} WHERE item_name LIKE '%{item_name}%' ORDER BY price LIMIT 1;"
        sql4 = f"SELECT price FROM {self.table_name} WHERE item_name LIKE '%{item_name}%' ORDER BY price DESC LIMIT 1"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql1)
            avg = cursor.fetchall()
            avg = avg[0]
            avg = avg[0]
            cursor.execute(sql2)
            count = cursor.fetchall()
            count = count[0]
            count = count[0]
            cursor.execute(sql3)
            MIN = cursor.fetchall()
            MIN = MIN[0]
            MIN = MIN[0]
            cursor.execute(sql4)
            MAX = cursor.fetchall()
            MAX = MAX[0]
            MAX = MAX[0]
            cursor.close()
            count = int(count)
            print("AVG", '%0.2f' % avg)
            print("MAX", MAX)
            print("MIN", MIN)
            print("Count", count)
            print("PriceNum", '%0.2f' % (count * avg))
            return count, avg, MAX, MIN

        except:
            print("Err")

    def is_select_bargain_list(self, item_name, count, avg, max, min):
        sql = f"SELECT weapon_name, float_range, bargain_price, weapon_float FROM {self.table_name} " \
              f"WHERE item_name LIKE '%{item_name}%'" \
              f"and (status = '购买成功' OR status = '求购成功') ORDER BY bargain_price desc"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            data = data
            cursor.close()
            for i in data:
                print(i)

            print("AVG", '%0.2f' % avg)
            print("MAX", max)
            print("MIN", min)
            print("Count", count)
            print("PriceNum", '%0.2f' % (count * avg))
        except:
            print("Err")

    def is_get_bargaindb_ordertime(self):
        cursor = self.db.cursor()
        sql = f"select order_time from {self.table_name} ORDER BY order_time DESC LIMIT 1 "
        try:
            cursor.execute(sql)
            time = cursor.fetchall()
            time = time[0]
            time = time[0]
            cursor.close()
            return time
        except Exception as e:
            print("数据库为空", e)
            temp_time = "1970-01-01 08:00:00"
            temp_time = datetime.strptime(temp_time, '%Y-%m-%d %H:%M:%S')
            return temp_time

    def is_get_selldb_ordertime(self):
        cursor = self.db.cursor()
        sql = f"select order_time from {self.sell_table_name} ORDER BY order_time DESC LIMIT 1 "
        try:
            cursor.execute(sql)
            time = cursor.fetchall()
            time = time[0]
            time = time[0]
            cursor.close()
            return time
        except Exception as e:
            print("数据库为空", e)
            temp_time = "1970-01-01 08:00:00"
            temp_time = datetime.strptime(temp_time, '%Y-%m-%d %H:%M:%S')
            return temp_time

    def is_get_steamdb_ordertime(self):
        cursor = self.db.cursor()
        sql = f"select trading_partners from {self.steam_record} ORDER BY trading_partners DESC LIMIT 1 "
        try:
            cursor.execute(sql)
            time = cursor.fetchall()
            time = time[0]
            time = time[0]
            cursor.close()
            return time
        except Exception as e:
            print("数据库为空", e)
            temp_time = "1970-01-01"
            temp_time = datetime.strptime(temp_time, '%Y-%m-%d')
            return temp_time

    def is_get_funds(self):
        sql = f"SELECT sum(amount) FROM {self.funds} WHERE type = 'in'"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            time = cursor.fetchall()
            time = time[0]
            time = time[0]
            cursor.close()
            return '%0.2f' % time
        except:
            return "ERR"

    def is_get_assets(self):
        sql = f" SELECT `value`, sum FROM assets WHERE type = 'in' "
        try:
            data = 0
            cursor = self.db.cursor()
            cursor.execute(sql)
            time = cursor.fetchall()
            cursor.close()
            for i in time:
                data += i[0] * i[1]
            return data
        except:
            return "ERR"

    def is_get_assets_list(self):
        sql = f"SELECT `name`, sum FROM assets WHERE type = 'in' "
        try:
            data = 0
            cursor = self.db.cursor()
            cursor.execute(sql)
            time = cursor.fetchall()
            cursor.close()
            for i in time:
                print[i]
        except:
            return "ERR"

    def is_get_withdraw(self):
        sql = f"SELECT sum(amount) FROM {self.funds} WHERE type = 'out'"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            time = cursor.fetchall()
            time = time[0]
            time = time[0]
            cursor.close()
            return time
        except:
            return "ERR"
