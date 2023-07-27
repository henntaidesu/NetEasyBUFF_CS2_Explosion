import getpass
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Model.SteamItem import SteamItem
from Utils import Utils


class BuyHistory:

    def __init__(self):
        self.driver = None
        self.options = webdriver.ChromeOptions()

        self.user_data_dir = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\Selenium User Data"

        # if not exits, create the user data dir
        if not os.path.exists(self.user_data_dir):
            os.makedirs(self.user_data_dir)

        self.options.add_argument(f"user-data-dir={self.user_data_dir}")
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def run(self) -> list[SteamItem]:
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://steamcommunity.com/market/")

        if not Utils.is_login(self.driver):
            self.driver.execute_script("document.querySelectorAll('body > div.header.responsive_page_frame with_header "
                                       "> responsive_page_content > responsive_page_template_content "
                                       "> pagecontent no_header > BG_bottom > mainContents > myListings "
                                       "> tabContentsMyMarketHistory > tabContentsMyMarketHistoryTable "
                                       "> tabContentsMyMarketHistoryRows "
                                       "div.nav.nav_entries > ul > li > a')[0].onclick()")
            print("Please login!!!")
            while True:
                if Utils.is_login(self.driver):
                    break
                sleep(1)

        self.driver.get(f"https://steamcommunity.com/market/")



