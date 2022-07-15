
import json
from os import environ
from etherchainpy import EtherChainPy


if __name__ == "__main__":

    ## Testing Blocks ...

    e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'])
    b = e.blocks.getBlockByNumber(blockno=2165403).json()
    #print(b)

    print(e.geth.getGasPrice(to="WEI"))
    print(e.geth.getGasPrice(to="GWEI"))
    print(e.geth.getGasPrice(to="ETH"))
    print(e.geth.getGasPrice(to="ZAR"))
