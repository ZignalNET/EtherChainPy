
import json
from os import environ
from etherchainpy import EtherChainPy


if __name__ == "__main__":

    ## Testing Logs ...

    e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'])
    l = e.logs.getLogsByAddressAndBlocks(address="0xbd3531da5cf5857e7cfaa92426877b022e612cf8").json()
    print(l)
