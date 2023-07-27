from Function.Function import GetMainUpdateDB, GetMainInsertDB, GetMainDeleteDB, GetMainSelectDB
import time
import os
import sys
getMainInsertDB = GetMainInsertDB()
getMainUpdateDB = GetMainUpdateDB()
getMainDeleteDB = GetMainDeleteDB()
getMainSelectDB = GetMainSelectDB()


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


class Index:

    def get_main_function(self):

        print("\n"
              "投资总量：", getMainSelectDB.get_funds(), "￥\n"
              "购买金额：", getMainSelectDB.get_select_bargain_price() + (21 * 500), "￥\n"
              "固定资产：", getMainSelectDB.get_assets(), "￥\n"
              "出售金额：", getMainSelectDB.get_select_sell_price(), "￥\n"
              "提现金额：", getMainSelectDB.get_withdraw(), "￥\n"
              "等待收货：", getMainSelectDB.get_select_bargain_wait(), "\n"
              )

        print(
            "1、写入BUFF购买数据\n"
            "2、写入BUFF出售数据\n"
            "3、写入Steam数据\n"
            "4、悠悠有品租赁数据\n"
            "7、删除未购买成功的物品\n"
            "8、查询特定商品\n"
            "9、打印购买数量\n"
            "a、写入投资数据\n"
            "z、重置购买库\n"
            "x、重置售出库\n"
        )

    def get_main_filg(self, flag):
        if flag == "0":
            exit(1)
        if flag == "1":
            getMainInsertDB.get_buy_item(getMainSelectDB.get_bargaindb_ordertime())
        if flag == "2":
            getMainInsertDB.get_sell_item(getMainSelectDB.get_selldb_ordertime())
        if flag == "3":
            getMainInsertDB.get_steam_item(getMainSelectDB.get_steam_trading_partners())
        if flag == "4":
            return True
        if flag == "7":
            getMainUpdateDB.get_update_buy()
        if flag == "8":
            getMainSelectDB.is_select_bargain_count()
        if flag == "9":
            getMainSelectDB.get_bargain_list_all()
        if flag == "a":
            getMainInsertDB.get_funds_item()
        if flag == 'b':
            getMainSelectDB.get_assets()
        if flag == "z":
            getMainDeleteDB.get_buy_delete()
        if flag == "x":
            getMainDeleteDB.get_sell_delete()
        if flag == "\n":
            return True

