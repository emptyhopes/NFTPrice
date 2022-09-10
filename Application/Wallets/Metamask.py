import sys
from Application.Modules.Utils import Utils

from Config.Config import Config

class Metamask:
    def __main__ (Driver):
        Metamask.Algorithm(Driver)

    def Algorithm (Driver):

        try:

            # Close extension window

            Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])
            Utils.CloseWindow(Driver.browser)
            Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])

            # Import wallet

            Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div/div/button')
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]')
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')

            for index, word in enumerate(Config.words):
                Utils.SendKeys(Driver.browser, '//*[@id="import-srp__srp-word-{}"]'.format(index), word, 0)

            Utils.SendKeys(Driver.browser, '//*[@id="password"]', Config.password)
            Utils.SendKeys(Driver.browser, '//*[@id="confirm-password"]', Config.password)
            Utils.Click(Driver.browser, '//*[@id="create-new-vault__terms-checkbox"]')
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button')
            Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/end-of-flow")
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div/button')
            Utils.Click(Driver.browser, '//*[@id="popover-content"]/div/div/section/div[1]/div/button')

            if Config.blockchain == "Rinkeby":
                Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/advanced")
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/label/div[1]')
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div')
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[2]/li[4]')

            if Config.blockchain == "Mumbai":
                Utils.Get(Driver.browser, "https://mumbai.polygonscan.com")
                Utils.ExecuteScript(Driver.browser, '//*[@id="body"]/footer/div/div[1]/div[2]/div/span/button')
                Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])
                Utils.SwitchNewWindow(Driver.browser)
                Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]')
                Utils.CloseWindow(Driver.browser)
                Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])

            if Config.blockchain == "Matic":
                Utils.Get(Driver.browser, "https://polygonscan.com/")
                Utils.ExecuteScript(Driver.browser, '//*[@id="body"]/footer/div/div[1]/div[2]/div/span/button')
                Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])
                Utils.SwitchNewWindow(Driver.browser)
                Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]')
                Utils.CloseWindow(Driver.browser)
                Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])

            # Login on Config.uri (testnets.opensea or opensea)

            Utils.Get(Driver.browser, Config.uri)
            Utils.Click(Driver.browser, '//*[@id="__next"]/div/div[1]/div/nav/ul/div[2]/div/div[2]/li/button')
            Utils.Click(Driver.browser, '//*[@id="__next"]/div/aside[2]/div[2]/div/div[2]/ul/li[1]/button')
            Utils.SwitchNewWindow(Driver.browser)
            Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]')
            Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
            Utils.CloseWindow(Driver.browser)
            Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])

            # Set price

            for index in range(Config.start, Config.end + 1):
                Utils.Get(Driver.browser, "{}/assets/{}/{}/{}/sell".format(Config.uri, Config.blockchain.lower(), Config.address, index))
                # Попробовать сделать выставление длительности
                # Utils.Click(Driver.browser, '//*[@id="duration"]')
                # Utils.Click(Driver.browser, '//*[@id="main"]/div/div/div[2]/div/div[1]/div/form/div[3]/div/div[1]')
                Utils.SendKeys(Driver.browser, '//*[@id="price"]', Config.price)
                Utils.Click(Driver.browser, '//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[6]/button')
                Utils.Sleep(1)
                Utils.SwitchNewWindow(Driver.browser)
                Utils.Get(Driver.browser, "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[3]/div/div[3]/div[1]')
                Utils.Click(Driver.browser, '//*[@id="app-content"]/div/div[3]/div/div[4]/button[2]')
                Utils.CloseWindow(Driver.browser)
                Utils.SwitchWindow(Driver.browser, Driver.browser.window_handles[0])

        except:
            Driver.browser.close()
            Driver.browser.quit()
            sys.exit(0)

        finally:
            Driver.browser.close()
            Driver.browser.quit()
            
            print("The program has ended.")

            sys.exit(0)