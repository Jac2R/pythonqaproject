import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



@pytest.fixture
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception:
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://practice-automation.com/form-fields/')
    yield driver
    wait = WebDriverWait(driver, 8)
    try:
        alert = wait.until(EC.alert_is_present())
        text = alert.text
        assert text == "Message received!"
        alert.accept()
    except TimeoutException:
        pytest.fail("Поле Name не заполнено или submit не сработал. Форма не отправилась")
    driver.close()