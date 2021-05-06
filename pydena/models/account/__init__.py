from pydantic import BaseModel
from typing import List

class Accounts(BaseModel):
    accounts: List[str] = None

    class Config:
        fields = {
            'accounts': 'result'
        }