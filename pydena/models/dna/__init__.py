from pydantic import BaseModel
from typing import List
from datetime import datetime

class Invitee(BaseModel):
    txHash: str
    address: str
    class Config:
        fields = {
            'txHash': 'TxHash',
            'address': 'Address'
        }

class Identity(BaseModel):
    address: str = None
    profileHas: str = None
    stake: str = None
    invites: int = 0
    age: int = 0
    state: str = None
    pubkey: str = None
    requiredFlips: int = 0
    availableFlips: int = 0
    flipKeyWordPairs: List[dict] = None
    madeFlips: int = 0
    totalQualifiedFlips: int = 0
    totalShortFlipPoints: int = 0
    flips: List[str] = None
    online: bool = False
    generation: int = 0
    code: str = None
    invitees: List[Invitee] = None
    penalty: str = None
    lastValidationFlags: List[str] = None
    delegatee: str = None
    delegationEpoch: int = 0
    delegationNonce: int = 0
    isPool: bool = False

class State(BaseModel):
    name: str = None

class Epoch(BaseModel):
    epoch: int = None
    nextValidation: datetime = None
    currentPeriod: str = None
    currentValidationStart: datetime = None

class CeremonyIntervals(BaseModel):
    flipLotteryDuration: int = None
    shortSessionDuration: int = None
    longSessionDuration: int = None

    class Config:
        fields = {
            'flipLotteryDuration': 'FlipLotteryDuration',
            'shortSessionDuration': 'ShortSessionDuration',
            'longSessionDuration': 'LongSessionDuration'
        }

class ProfileTxn(BaseModel):
    txHash: str
    hash: str

class Profile(BaseModel):
    info: str
    nickname: str

class RandomInviteTxn(BaseModel):
    hash: str
    address: str
    key: str