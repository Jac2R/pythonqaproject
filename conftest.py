from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get('https://practice-automation.com/form-fields/')
    yield driver
    wait = WebDriverWait(driver, 50)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    assert text == "Message received!"
    alert.accept()
    driver.close()