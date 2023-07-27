import datetime
from datetime import datetime
from BuffRecorder.SellHistory import SellOrderItem
from BuffRecorder.BuyHistory import BuyHistory
from BuffRecorder.SteamItem import SteamItem
from SQL.InsterDB import InsterDB
from SQL.SelectDB import SelectDB
from SQL.DeleteDB import DeleteDB
from SQL.UpdateDB import UpdateDB
updateDB = UpdateDB()
insterDB = InsterDB()
deleteDB = DeleteDB()
selectDB = SelectDB()


class GetMainUpdateDB:

    def get_update_buy(self):
        updateDB.get_update_buy()


class GetMainInsertDB:

    def get_buy_item(self, ordertime):
        # print(ordertime)
        statistics = 0
        deleteDB.delete_buy_order_time_limit1(ordertime)
        buy_history = BuyHistory()
        for item in buy_history.run(current_page_num=1):
            flag = insterDB.insert_buff_buy_item(item, ordertime)
            statistics += 1
            if not flag:
                print("共写入数据：", statistics - 2, "条")
                print("已全部写入")
                return False


    def get_sell_item(self, ordertime):
        # print(ordertime)
        deleteDB.delete_buy_sell_time_limit1(ordertime)
        sell_order_item = SellOrderItem()
        for item in sell_order_item.run(current_page_num=1):
            flag = insterDB.insert_buff_sell_item(item, ordertime)
            if not flag:
                print("已全部写入")
                return False

    def get_steam_item(self, ordertime):
        # print(ordertime)
        deleteDB.delete_buy_sell_time_limit1(ordertime)
        sell_steam_item = SteamItem()
        for item in sell_steam_item.run():
            flag = insterDB.insert_buff_sell_item(item, ordertime)
            if not flag:
                print("已全部写入")
                return False

    def get_funds_item(self):
        global type, funds
        print("1、aliplay\n"
              "2、wechat \n"
              "3、steam  \n")
        flag = input()
        if flag == "1":
            funds = 'aliplay'
        if flag == "2":
            funds = 'wechat'
        if flag == "3":
            funds = 'steam'
        print("1、in\n"
              "2、out \n")
        flag = input()
        if flag == "1":
            type = 'in'
        if flag == "2":
            type = 'out'
        while True:
            print("pless input amount\n")
            amount = input(float)
            if amount == 0:
                break
            date = datetime.now()
            insterDB.insert_funds_item(funds, type, amount, date)


class GetMainDeleteDB:

    def get_buy_delete(self) -> bool:
        print("1:YES\n"
              "2:exit")
        ff = int(input())
        if ff == 1:
            status = deleteDB.delete_buy_item()
            if status != 0:
                print("Delete success")
            if status == 0:
                print("Delete fail")
        if ff == 2:
            return False

    def get_sell_delete(self) -> bool:
        print("1:YES\n"
              "2:exit")
        ff = int(input())
        if ff == 1:
            status = deleteDB.delete_sell_item()
            if status != 0:
                print("Delete success")
            if status == 0:
                print("Delete fail")
        if ff == 2:
            return False


class GetMainSelectDB:

    def get_select_bargain_price(self):
        return selectDB.is_select_bargain_price()

    def get_select_sell_price(self):
        return selectDB.is_select_sell_price()

    def get_select_bargain_wait(self):
        return selectDB.is_select_bargain_wait()

    def is_select_bargain_count(self):
        while True:
            print("输入需要查询的项目")
            item = input()
            if item == "0":
                break
            else:
                count, avg, MAX, MIN = selectDB.is_select_bargain_count(item)
                if count < 100:
                    selectDB.is_select_bargain_list(item, count, avg, MAX, MIN)

    def get_bargain_list_all(self):
        selectDB.is_get_bargain_list_all()

    def get_bargaindb_ordertime(self):
        return selectDB.is_get_bargaindb_ordertime()

    def get_selldb_ordertime(self):
        return selectDB.is_get_selldb_ordertime()

    def get_steam_trading_partners(self):
        return selectDB.is_get_steamdb_ordertime()

    def get_funds(self):
        return selectDB.is_get_funds()

    def get_assets(self):
        return selectDB.is_get_assets()

    def get_withdraw(self):
        return selectDB.is_get_withdraw()



