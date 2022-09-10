from Application.Modules.Driver import Driver
from Application.Wallets.Metamask import Metamask

from Config.Config import Config

def __main__ ():
    Driver.__main__()

    if Config.wallet == "Metamask":
        Metamask.__main__(Driver)