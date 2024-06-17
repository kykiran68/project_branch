import pytest
from module.page_module_class import TechmintSmartLearningManagementSystem
from data.test_data import *

@pytest.mark.usefixtures("get_driver")
class TestTechmintSmartLearning:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.tsls = TechmintSmartLearningManagementSystem(self.driver)
    def test_Techmint_Smart(self):
        self.tsls.enter_mobile_no(mobile_no)

        self.tsls.click_button_otp()

        self.tsls.enter_otp1(otp1)
        self.tsls.enter_otp2(otp2)
        self.tsls.enter_otp3(otp3)
        self.tsls.enter_otp4(otp4)
        self.tsls.enter_otp5(otp5)
        self.tsls.enter_otp6(otp6)

        self.tsls.click_verify_otp()

        self.tsls.click_on_profile()

        self.tsls.click_administrator()
        self.tsls.click_sidebar()

        self.tsls.click_view_all()

        self.tsls.click_on_school_leaving()

        self.tsls.generate_certificate()

#        self.tsls.click_checkbox()
        self.tsls.click_generate()

        self.tsls.enter_remark(put_remark)

        self.tsls.click_on_button()

        self.tsls.click_download()
