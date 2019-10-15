# 雪球首页
from time import sleep

from appium_po.page.profile_page import ProfilePage
from appium_po.page.search_page import SearchPage
from appium import webdriver


class XueqiuPage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "abc"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def goto_search(self):
        self.driver.find_element_by_id("tv_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        sleep(15)
        self.driver.find_element_by_id("user_profile_icon").click()
        return ProfilePage(self.driver)


