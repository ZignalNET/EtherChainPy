
import json
from os import environ
from etherchainpy import EtherChainPy


if __name__ == "__main__":

	##
    ## Testing Account balances ...
    ##


    e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'])

    #Single address
    balance = e.accounts.balance("0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae","latest")
    gwei = balance.toGWEI()
    eth  = balance.toETH()
    zar  = balance.toZAR()
    eur  = balance.toFIAT(value=eth, to="EUR")

    print(gwei)
    print(eth)
    print(zar)
    print(eur)
    
    #Multi addresses
    balances = e.accounts.balances(["0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a","0x63a9975ba31b0b9626b34300f7f627147df1f526"],"latest")
    gwei = balances.toGWEI()
    eth  = balances.toETH()
    fiat = balances.toZAR()
    cad = balances.toFIAT(value=eth, to="CAD")

    print(gwei)
    print(eth)
    print(fiat)
    print(cad)
    

   


