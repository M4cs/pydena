# pydena

Unofficial Python API for [idena-go RPC](https://github.com/idena-network/idena-go)

# Requirements

- Python 3.6+

# Installation

```
# From pypi
pip install pydena

# From source
git clone github.com/M4cs/pydena
cd pydena
python3 setup.py install
```

# Roadmap

**RPC APIs:**

- [X] IPFS API ✔
- [X] Accounts API ✔
- [X] Blockchain API ✔
- [X] DNA API ✔
- [ ] Net API ❌
- [ ] Flip API ❌
- [ ] Contracts API ❌

**Idena API:**

This will be worked on after RPC. Version 2 will migrate API -> pydena.RPC. pydena.API will become the http API for the explorer.

# Usage

**Initialize your API:**

```py
from pydena import API

# Local Node with No API Key on http://localhost:9009
api = API()

# Local Node with API Key
api = API(apikey='YOUR-API-KEY')

# Remote node with API Key
api = API('http://localhost:9999', 'YOUR-API-KEY')

# Get Coinbase Address:
api.getCoinbaseAddress()

# Get Last Block:
api.getLastBlock()

# See all in documentation below!
```

### View the official documentation [here](https://m4cs.github.io/pydena/)
