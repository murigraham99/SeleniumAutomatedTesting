import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

import app


# TEST THE LOGIN PAGE
class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.chrome_driver_path = "/Users/robertmuresan/PycharmProjects/chromedriver"
        self.driver = webdriver.Chrome()

    def test_login_active_user(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_login_page()
        login_page.enter_username("test")
        login_page.enter_password("test")
        login_page.press_submit()
        redirect_url = login_page.get_redirect_url()

        self.assertIn("select_period", redirect_url, "Not in url")

    def test_login_wrong_username(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_login_page()
        login_page.enter_username("wrongusername")
        login_page.enter_password("wrongpassword")
        login_page.press_submit()
        error_msg = login_page.get_error_message()

        self.assertIn("Username not existing!", error_msg, "Not in error message!")

    def test_login_wrong_password(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_login_page()
        login_page.enter_username("test")
        login_page.enter_password("wrongpassword")
        login_page.press_submit()
        error_msg = login_page.get_error_message()

        self.assertIn("Wrong password!", error_msg, "Not in error message!")

    def test_signup_link(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_login_page()
        sign_up_link_redirect = login_page.go_to_signup_link()

        self.assertIn("sign_up", sign_up_link_redirect, "Not in Sign up!")

    def tearDown(self):
        self.driver.quit()


# TEST THE SIGNUP PAGE
class TestSignupPage(unittest.TestCase):
    def setUp(self):
        self.chrome_driver_path = "/Users/robertmuresan/PycharmProjects/chromedriver"
        self.driver = webdriver.Chrome()

    def test_successful_creation(self):
        signup_page = SignupPage(self.driver)
        signup_page.go_to_signup_page()
        signup_page.enter_username(f"username{random.randint(0, 99999999)}.success")
        signup_page.enter_email(f"username{random.randint(0, 99999999)}.@success")
        signup_page.enter_password("test")
        signup_page.press_create_account_btn()
        redirect_url = signup_page.get_redirect_url()

        self.assertIn("select_period", redirect_url, "Not in url")

    def test_username_already_used(self):
        signup_page = SignupPage(self.driver)
        signup_page.go_to_signup_page()
        signup_page.enter_username("test")
        signup_page.enter_email(f"username{random.randint(0, 99999999)}.@success")
        signup_page.enter_password("test")
        signup_page.press_create_account_btn()
        error_msg = signup_page.get_error_message()

        self.assertIn("Username already used.", error_msg, "Not in error message")

    def test_email_already_used(self):
        signup_page = SignupPage(self.driver)
        signup_page.go_to_signup_page()
        signup_page.enter_username(f"username{random.randint(0, 99999999)}.success")
        signup_page.enter_email("r@r")
        signup_page.enter_password("test")
        signup_page.press_create_account_btn()
        error_msg = signup_page.get_error_message()

        self.assertIn("Email already used.", error_msg, "Not in error message")

    def test_login_link(self):
        signup_page = SignupPage(self.driver)
        signup_page.go_to_signup_page()
        login_link_redirect = signup_page.go_to_login_link()

        self.assertIn("login", login_link_redirect, "Not in Sign up!")

    def tearDown(self):
        self.driver.quit()


# TEST THE SELECT PERIOD PAGE
class TestSelectPeriod(unittest.TestCase):
    def setUp(self):
        self.chrome_driver_path = "/Users/robertmuresan/PycharmProjects/chromedriver"
        self.driver = webdriver.Chrome()

    def test_pre_button(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        pre_redirect_url = select_period_page.go_to_pre_button()
        print(pre_redirect_url)
        self.assertIn("guessing_game/prehistory", pre_redirect_url)

    def test_ancient_button(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        anc_redirect_url = select_period_page.go_to_ancient_button()
        self.assertIn("guessing_game/ancient%20history", anc_redirect_url)

    def test_pch_button(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        pch_redirect_url = select_period_page.go_to_pch_button()
        self.assertIn("guessing_game/post-classical%20history", pch_redirect_url)

    def test_modern_button(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        modern_redirect_url = select_period_page.go_to_modern_button()
        self.assertIn("guessing_game/modern%20history", modern_redirect_url)

    def test_pre_image(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        pre_redirect_url = select_period_page.go_to_pre_image()
        self.assertIn("guessing_game/prehistory", pre_redirect_url)

    def test_ancient_image(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        anc_redirect_url = select_period_page.go_to_anc_image()
        self.assertIn("guessing_game/ancient%20history", anc_redirect_url)

    def test_pch_image(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        pch_redirect_url = select_period_page.go_to_pch_image()
        self.assertIn("guessing_game/post-classical%20history", pch_redirect_url)

    def test_modern_image(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        modern_redirect_url = select_period_page.go_to_modern_image()
        self.assertIn("guessing_game/modern%20history", modern_redirect_url)

    def tearDown(self):
        self.driver.quit()


class TestMultipleChoice(unittest.TestCase):
    def setUp(self):
        self.chrome_driver_path = "/Users/robertmuresan/PycharmProjects/chromedriver"
        self.driver = webdriver.Chrome()

    def test_hint(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        select_period_page.go_to_pre_image()
        multiple_choice = MultipleChoicePage(self.driver)
        in_choices = False
        if multiple_choice.get_hint() in multiple_choice.get_options():
            in_choices = True

        self.assertEqual(in_choices, False)

    def test_correct_ans(self):
        login = LoginPage(self.driver)
        login.go_to_login_page()
        login.enter_username("test")
        login.enter_password("test")
        login.press_submit()
        select_period_page = SelectPeriodPage(self.driver)
        select_period_page.go_to_pre_image()
        multiple_choice = MultipleChoicePage(self.driver)
        correct_url = multiple_choice.click_correct_answer()
        print(correct_url)

        self.assertIn("", correct_url)

    def tearDown(self):
        self.driver.quit()


########################################################################################################################
########################################################################################################################

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get("http://127.0.0.1:3000/login")

    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    def press_submit(self):
        button = self.driver.find_element(By.CLASS_NAME, "btn")
        button.click()

    def get_redirect_url(self):
        time.sleep(1)
        url = self.driver.current_url
        return url

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error").text

    def go_to_signup_link(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/p/a").click()
        return self.driver.current_url


class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_signup_page(self):
        self.driver.get("http://127.0.0.1:3000/sign_up")

    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(username)

    def enter_email(self, email):
        password_field = self.driver.find_element(By.ID, "email")
        password_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    def press_create_account_btn(self):
        button = self.driver.find_element(By.CLASS_NAME, "btn")
        button.click()

    def get_redirect_url(self):
        time.sleep(1)
        url = self.driver.current_url
        return url

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error").text

    def go_to_login_link(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/p/a").click()
        return self.driver.current_url


class SelectPeriodPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_select_period(self):
        self.driver.get("http://127.0.0.1:3000/select_period")

    def go_to_pre_button(self):
        button_pre = self.driver.find_element(By.ID, "buttonPre")
        button_pre.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_ancient_button(self):
        button_anc = self.driver.find_element(By.ID, "buttonAncient")
        button_anc.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_pch_button(self):
        button_pch = self.driver.find_element(By.ID, "buttonPCH")
        button_pch.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_modern_button(self):
        button_modern = self.driver.find_element(By.ID, "buttonModern")
        button_modern.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_pre_image(self):
        image_pre = self.driver.find_element(By.XPATH, "/html/body/div[1]/a[1]")
        image_pre.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_anc_image(self):
        image_anc = self.driver.find_element(By.XPATH, "/html/body/div[1]/a[2]")
        image_anc.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_pch_image(self):
        image_pch = self.driver.find_element(By.XPATH, "/html/body/div[1]/a[3]")
        image_pch.click()
        time.sleep(10)
        return self.driver.current_url

    def go_to_modern_image(self):
        image_modern = self.driver.find_element(By.XPATH, "/html/body/div[1]/a[4]")
        image_modern.click()
        time.sleep(10)
        return self.driver.current_url


class MultipleChoicePage:
    def __init__(self, driver):
        self.driver = driver

    def get_hint(self):
        hint_but = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/a")
        hint_but.click()
        hint = self.driver.find_element(By.XPATH, '//*[@id="hints"]/p')
        return hint.text

    def get_options(self):
        options = []
        options_raw = self.driver.find_elements(By.CSS_SELECTOR, "option")
        for option in options_raw:
            options.append(option.text)

        return options

    def get_correct_answer(self):
        correct_ans = self.driver.find_element(By.ID, "demo")
        button = self.driver.find_element(By.XPATH, f"//option[text()='{correct_ans.text}']")
        print(str(button.text))
        print(correct_ans.text)
        print(button.text == correct_ans.text)

        return correct_ans.text

    def click_correct_answer(self):
        button = self.driver.find_element(By.XPATH, f"//option[text()='{self.get_correct_answer()}']")
        print(button)
        button.click()
        button.click()
        time.sleep(10)
        return self.driver.current_url


if __name__ == '__main__':
    unittest.main()
