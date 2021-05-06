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

- [X] IPFS API ✔
- [X] Accounts API ✔
- [X] DNA API ✔
- [ ] Blockchain API (Partially Complete) 💻
- [ ] Contracts API ❌

# Usage

**Initialize your API:**

```py
from pydena import API

api = API('http://localhost:9999', 'YOUR-API-KEY')
```

**Use the provided API calls:**

```py
# Get Coinbase Address:
api.getCoinbaseAddress()

# Get Last Block:
api.getLastBlock()
```

### View the official documentation [here](https://m4cs.github.io/pydena/)
