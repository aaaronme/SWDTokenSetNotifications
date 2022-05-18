

import json
from decimal import Decimal
from web3 import Web3

def getABI():
    with open("abi.json") as f:
        return json.load(f)



def convert(amount):
    #: Convert gwei to wei
    # wei_amount = Decimal(amount) * (Decimal(10) ** 9)  # Gigaweis are billions
    eth_amount = Web3.fromWei(amount,'ether')
    return eth_amount