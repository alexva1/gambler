from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time



def get_shadow_root(element):
    return driver.execute_script('return arguments[0].shadowRoot', element)

USERNAME = "dsfsdaf@hotmail.com"
PASSWORD = "asdfadsf"

options = Options()
driver = uc.Chrome(driver_executable_path='drivers/chromedriver.exe', options=options)
driver.set_window_size(500,500)
driver.set_window_position(0,0)

# Open stoiximan page
driver.get("https://www.stoiximan.gr/")

x_button = driver.find_element(By.CLASS_NAME, 'sb-modal__close__btn')
x_button.click()

shadow_host = driver.find_element(By.XPATH, '//kaizen-header')
login_button = get_shadow_root(shadow_host).find_element(By.CSS_SELECTOR, '[data-qa="login-button"]')
login_button.click()

iframe = driver.find_element(By.CSS_SELECTOR , 'iframe[src="/myaccount/login"]')
driver.switch_to.frame(iframe)
username_field = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, 'username'))
)
username_field.send_keys(USERNAME)
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(PASSWORD)
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="submit"]')
submit_button.click()
driver.switch_to.default_content()
time.sleep(100)