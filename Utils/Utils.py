import locale
import os
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Model.HistoryItem import HistoryItem

LANG = 'en'

try:
    locale.getdefaultlocale()[0].index('en')
    LANG = 'en'
    LANG_FLOAT = 'Float'
except ValueError:
    LANG = 'zh'
    LANG_FLOAT = '磨损'


class Status:
    wait_offer = '等待卖家回应报价查看报价'
    buy_success = '购买成功'


def kill_chrome_process():
    os.system("taskkill /f /im chrome.exe")


def is_name_float(name: str) -> bool:
    try:
        name.split('\n')[1].index(LANG_FLOAT)
        return True
    except Exception:
        return False


def is_price(price: str) -> bool:
    try:
        price.index("¥")
        return True
    except ValueError:
        return False


def is_bargain_price(price: str) -> bool:
    if len(price.split('\n')) > 1:
        return True
    else:
        return False


def get_bargain_price(price: str) -> float:
    return float(price.split('\n')[1].replace("¥", "").strip())


def get_weapon_info(info: str) -> tuple[str, str, float, str]:
    weapon = info.split('\n')[0].split('|')[0].strip()
    item_name = info.split('\n')[0].split('|')[1].strip().split('(')[0].strip()
    weapon_float = float(info.split('\n')[1].replace(f"{LANG_FLOAT}:", "").strip())
    float_range = info.split('|')[1].split('(')[1].split(')')[0].strip()
    return weapon, item_name, weapon_float, float_range


def is_item_exist(item_buy_time: str) -> bool:
    return False


def is_datetime(info: str) -> bool:
    if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', info):
        return True
    else:
        return False


def is_login(driver: webdriver) -> bool:
    wait = WebDriverWait(driver, 10)
    element = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, "body > div.header.l_Clearfix > div > div.nav.nav_entries > ul > li > a")))
    try:
        driver.execute_script("return arguments[0].onclick.toString().indexOf('showLogin') > 0;", element)
        return False
    except:
        return True


def get_page_data(driver: webdriver) -> list[HistoryItem]:

    try:
        # get tbody by class name
        tbody = driver.find_element(By.CLASS_NAME, value="list_tb_csgo")
        history_item = []
        history_items = []
        # foreach tbody
        for tr in tbody.find_elements(By.TAG_NAME, value="tr"):
            item_buy_time = '0000-00-00 00:00:00'
            try:
                str(tr.text).index(LANG_FLOAT)
                is_weapon = True
            except ValueError:
                is_weapon = False

            for td in tr.find_elements(By.TAG_NAME, value="td"):
                if td.text == "":
                    continue
                else:
                    if is_datetime(td.text):
                        item_buy_time = td.text
                    if is_weapon:
                        if is_name_float(td.text):
                            weapon_name, item_name, float_range, weapon_float = get_weapon_info(td.text)
                            history_item.append(weapon_name)
                            history_item.append(item_name)
                            history_item.append(float_range)
                            history_item.append(weapon_float)
                            continue
                        elif is_price(td.text):
                            history_item.append(float(td.text.split('\n')[0].replace('¥', '').strip()))
                            if is_bargain_price(td.text):
                                history_item.append(get_bargain_price(td.text))
                            else:
                                history_item.append(float(td.text.replace('¥', '').strip()))
                            continue
                        history_item.append(td.text)
                        if len(history_item) >= 10:
                            break
                    else:
                        if is_price(td.text):
                            history_item.append(float(td.text.split('\n')[0].replace('¥', '').strip()))
                            if is_bargain_price(td.text):
                                history_item.append(get_bargain_price(td.text))
                            else:
                                history_item.append(float(td.text.replace('¥', '').strip()))
                            continue
                        history_item.append(td.text)
                        if len(history_item) >= 10:
                            break

            if is_item_exist(item_buy_time):
                print("Update complete! Found a item that already exist in database!")
                exit(0)

            if not is_weapon:
                item_detail = HistoryItem(weapon_name=history_item[0], item_name=history_item[0], float_range='',
                                          weapon_float=0, price=history_item[1], bargain_price=history_item[2],
                                          seller_name=history_item[3], order_time=history_item[4],
                                          status=history_item[5])
                # print(item_detail)
                history_items.append(item_detail)
            else:
                item_detail = HistoryItem(*history_item)
                # print(item_detail)
                history_items.append(item_detail)
            yield item_detail
            history_item.clear()
    except:
        print("err")

    # return history_items
