import os
import time

from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait as WebdriverWait
from selenium.webdriver.common.by import By

class Utils:

    def Clear ():
        os.system("cls")
        time.sleep(1)

    def Sleep (value):
        time.sleep(value)

    def SwitchWindow (browser, handle, sleep = 1):
        browser.switch_to.window(handle)
        Utils.Sleep(sleep)

    def SwitchNewWindow (browser, sleep = 1):
        browser.switch_to.new_window("tab")
        Utils.Sleep(sleep)
        
    def CloseWindow (browser, sleep = 1):
        browser.close()
        Utils.Sleep(sleep)

    def Get (browser, url, sleep = 1):
        browser.get(url)
        Utils.Sleep(sleep)

    def Click (browser, xpath, sleep = 1):
        browser.find_element(By.XPATH, xpath).click()
        Utils.Sleep(sleep)

    def SendKeys (browser, xpath, value, sleep = 1):
        browser.find_element(By.XPATH, xpath).send_keys(value)
        Utils.Sleep(sleep)

    def ExecuteScript (browser, xpath, sleep = 1):
        browser.execute_script("arguments[0].click();", WebdriverWait(browser, 20).until(ExpectedConditions.element_to_be_clickable((By.XPATH, xpath))))
        Utils.Sleep(sleep)