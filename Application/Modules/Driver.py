from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from Config.Config import Config

class Driver:
    options = Options()
    browser = ""

    def __main__ ():
        Driver.Init()

    def Init ():
        Driver.options.add_argument("--start-maximized")
        Driver.options.add_extension(Config.extension)

        Driver.browser = webdriver.Chrome(Config.driver, options = Driver.options)