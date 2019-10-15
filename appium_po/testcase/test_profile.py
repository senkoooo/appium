from appium_po.page.xueqiu_page import XueqiuPage


class TestProfile:
    def setup(self):
        self.xueqiu = XueqiuPage()

    # 用户名错误

    def test_login_wrong_phone(self):
        assert "用户名或密码错误" in self.xueqiu.goto_profile().phone_login().phone_password().import_phone_and_password(
            "18292045414", "aiba1234").login_click()

    # 密码错误

    def test_login_wrong_password(self):
        assert "用户名或密码错误" in self.xueqiu.goto_profile().phone_login().phone_password().import_phone_and_password(
            "18292045410", "aiba1234").login_click()
