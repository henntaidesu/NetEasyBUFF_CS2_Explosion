import getpass
import json
import os
import getpass
import os
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Model.SellItem import SellItem
from Utils import Utils


class SellOrderItem:
    def __init__(self):
        self.driver = None
        self.options = webdriver.ChromeOptions()

        self.user_data_dir = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\Selenium User Data"

        # if not exits, create the user data dir
        if not os.path.exists(self.user_data_dir):
            os.makedirs(self.user_data_dir)

        self.options.add_argument(f"user-data-dir={self.user_data_dir}")
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def run(self, current_page_num: int = 1) -> list[SellItem]:
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://buff.163.com/")

        if not Utils.is_login(self.driver):
            self.driver.execute_script("document.querySelectorAll('body > div.header.l_Clearfix > div > "
                                       "div.nav.nav_entries > ul > li > a')[0].onclick()")
            print("Please login!!!")
            while True:
                if Utils.is_login(self.driver):
                    break
                sleep(1)

        self.driver.get(f"https://buff.163.com/market/sell_order/history?game=csgo&page_num={current_page_num}")

        history_items = []

        # get maximum page num, class name list-pager and tag name li

        try:
            pager = self.driver.find_element(By.CLASS_NAME, value="light-theme")
        except NoSuchElementException:
            pager = None

        if pager is not None:
            # get the last page num
            max_page_num = int(pager.find_elements(By.TAG_NAME, value="li")[-2].text)
        else:
            max_page_num = 1

        while current_page_num <= max_page_num:
            print("current page num: " + str(current_page_num), ", max page num: " + str(max_page_num))
            # click the next page
            # ret_history_items = Utils.get_page_data(self.driver)
            # history_items.extend(ret_history_items)
            for item in Utils.get_page_data(self.driver):
                yield item
            # scroll to the page bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

            if pager is not None:
                # click the next page via javascript
                self.driver.execute_script("document.getElementsByClassName('next')[0].click()")
                # get max page num via javascript
                max_page_num = int(self.driver.execute_script(
                    "return document.getElementsByClassName('light-theme')[0].getElementsByTagName('li')"
                    "[document.getElementsByClassName('light-theme')[0].getElementsByTagName('li').length - 2].innerText"))
            current_page_num += 1
