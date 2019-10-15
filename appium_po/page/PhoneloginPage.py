from appium_po.page.BasePage import BasePage


class PhoneloginPage(BasePage):
    def phone_password(self):
        self.driver.find_element_by_id("tv_login_with_account").click()
        return self

    def import_phone_and_password(self, phone, passw):
        self.driver.find_element_by_id("login_account").send_keys(phone)
        self.driver.find_element_by_id("login_password").send_keys(passw)
        return self

    def login_click(self):
        self.driver.find_element_by_id("button_next").click()
        text = self.driver.find_element_by_id("md_content").text
        return text
