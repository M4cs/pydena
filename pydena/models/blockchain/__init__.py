from pydantic import BaseModel
from typing import List

class Block(BaseModel):
    coinbase: str = None
    hash: str = None
    parentHash: str = None
    height: int = None
    timestamp: int = None
    root: str = None
    identityRoot: str = None
    ipfsCid: str = None
    transactions: list = None
    flags: list = None
    isEmpty: bool = None
    offlineAddress: str = None


class Transaction(BaseModel):
    hash: str = None
    type: str = None
    from_: str = None
    to: str = None
    amount: str = None
    tips: str = None
    maxFee: str = None
    nonce: int = None
    epoch: int = None
    payload: str = None
    blockHash: str = None
    usedFee: str = None
    timestamp: int = None

    class Config:
        fields = {
            'from_': 'from'
        }

class Mempool(BaseModel):
    results: list = []

class Sync(BaseModel):
    syncing: bool = False
    currentBlock: int = None
    highestBlock: int = None
    wrongTime: bool = False
    genesisBlock: int = None

class AddressTxns(BaseModel):
    transactions: List[Transaction] = []
    token: str = None

class BurntCoin(BaseModel):
    address: str = None
    amount: str = None
    key: int = None

class BurntCoins(BaseModel):
    results: List[BurntCoin] = None

class FlipKeyword(BaseModel):
    name: str = None
    desc: str = None
    
    class Config:
        fields = {
            'name': 'Name',
            'desc': 'Desc'
        }