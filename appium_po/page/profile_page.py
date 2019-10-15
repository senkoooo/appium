# 登录页
from time import sleep

from appium_po.page.BasePage import BasePage
from appium_po.page.PhoneloginPage import PhoneloginPage


class ProfilePage(BasePage):
    def phone_login(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("iv_login_phone").click()
        return PhoneloginPage(self.driver)
