from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure

class FormFieldsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Name Field')
    def name_field(self, name):
        wait = WebDriverWait(self.driver, 20)
        check_name_field_id = (By.ID, 'name-input')
        type_name = wait.until(EC.presence_of_element_located(check_name_field_id))
        type_name.send_keys(name)

    @allure.step('Password Field')
    def password_field(self, password):
        wait = WebDriverWait(self.driver, 20)
        check_password_field_css = (By.CSS_SELECTOR, 'input[type="password"]')
        type_password = wait.until(EC.presence_of_element_located(check_password_field_css))
        type_password.send_keys(password)

    @allure.step('Favorite Drink')
    def favorite_drink(self, drink):
        wait = WebDriverWait(self.driver, 20)
        check_favorite_drink_css = (By.CSS_SELECTOR, f"[value='{drink}' i]")
        drink_name = wait.until(EC.presence_of_element_located(check_favorite_drink_css))
        drink_name.click()

    @allure.step('Favorite Color')
    def favorite_color(self, color):
        wait = WebDriverWait(self.driver, 20)
        check_favorite_color_css = (By.CSS_SELECTOR, f"[value='{color}' i]")
        color_name = wait.until(EC.presence_of_element_located(check_favorite_color_css))
        color_name.click()

    @allure.step('Select Automation')
    def select_automation(self, any_automation):
        wait = WebDriverWait(self.driver, 20)
        check_selection_id = (By.ID, "automation")
        dropdown = wait.until(EC.presence_of_element_located(check_selection_id))
        select_auto = Select(dropdown)
        select_auto.select_by_value(any_automation)

    @allure.step('Email Field')
    def email_field(self, email):
        wait = WebDriverWait(self.driver, 20)
        check_email_field_xpath = (By.XPATH, "//input[@name='email']")
        type_email = wait.until(EC.presence_of_element_located(check_email_field_xpath))
        type_email.send_keys(email)

    @allure.step('Automation Tools')
    def automation_tools(self):
        wait = WebDriverWait(self.driver, 20)
        tools_locator = (By.XPATH, "//ul/following::li")
        find_tools = wait.until(EC.presence_of_all_elements_located(tools_locator))
        tools = [el.text for el in find_tools]

        count = len(tools)
        longest_tool = max(tools, key=len)
        message = f"{count}, {longest_tool}"

        message_field_id = (By.ID, "message")
        message_type = wait.until(EC.presence_of_element_located(message_field_id))
        message_type.send_keys(message)

    @allure.step('Submit Button')
    def submit_button(self):
        wait = WebDriverWait(self.driver, 20)
        check_submit_button_id = (By.ID, "submit-btn")
        check_submit_btn = wait.until(EC.presence_of_element_located(check_submit_button_id))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", check_submit_btn)
        sleep(0.3)
        check_submit_btn = wait.until(EC.element_to_be_clickable(check_submit_button_id))
        check_submit_btn.click()
