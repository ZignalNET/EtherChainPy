
import json
from os import environ
from etherchainpy import EtherChainPy


if __name__ == "__main__":

    ## Testing Geth ...

    e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'])
    b = e.geth.getTransactionByHash(txhash="0x111ae3586321f205dfc52c0a8143091973c0c9c9bdd4b3128cdf930dc5633ffc").json()
    
    print(b)
    
