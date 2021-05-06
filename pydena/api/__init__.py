from requests import Session
from pydena.models import AddressTxns, Block, Mempool, Sync, Transaction, BurntCoins, FlipKeyword, Identity, State, Accounts

class API(object):
    def __init__(self, host="http://localhost:9009", apikey=""):
        self.host = host
        if not host.startswith('http://'):
            self.host = 'http://' + host
        self.apikey = apikey
        self.session = Session()
        self.base_payload = {
            'params': [],
            'id': 1,
            'key': apikey,
            'method': ''
        }
        self.current_id = 1
    
    def _request(self, method, params=[]):
        payload = self.base_payload.copy()
        payload['id'] = self.current_id
        payload['params'] = params
        payload['method'] = method
        res = self.session.get(self.host, json=payload, timeout=30)
        self.current_id += 1
        return res

    def getLastBlock(self, raw=False):
        """Returns last block from node

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            block(Block): A block model holding block info
        
        """
        res = self._request('bcn_lastBlock')
        if raw:
            return res.json()
        return Block(**res.json().get('result'))
    
    def getBlockByHeight(self, height: int, raw=False):
        """Returns block by height

        Parameters:
            height(int): Height of block to search for
            raw(bool): Return in JSON format. Default: false

        Returns:
            block(Block): A block model holding block info
        
        """
        res = self._request('bcn_blockAt', [height])
        if raw:
            return res.json()
        return Block(**res.json().get('result'))

    def getBlockByHash(self, hash: str, raw=False):
        """Returns block by hash

        Parameters:
            hash(int): Hash of block to search for
            raw(bool): Return in JSON format. Default: false

        Returns:
            block(Block): A block model holding block info
        
        """
        res = self._request('bcn_block', [hash])
        if raw:
            return res.json()
        return Block(**res.json().get('result'))

    def getTransaction(self, hash: str, raw=False):
        """Gets transacation by txn hash

        Parameters:
            hash(int): Hash of txn to search for
            raw(bool): Return in JSON format. Default: false

        Returns:
            txn(Transaction): A transaction model holding transaction info
        
        """
        res = self._request('bcn_transaction', [hash])
        if raw:
            return res.json()
        return Transaction(**res.json().get('result'))

    def getMempool(self, raw=False):
        """Gets mempool information

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            txn(Transaction): A mempool model holding mempool info
        
        """
        res = self._request('bcn_mempool')
        if raw:
            return res.json()
        return Mempool(**res.json().get('result'))

    def checkSync(self, raw=False):
        """Gets syncronization information

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            sync(Sync): A sync model holding sync info
        
        """
        res = self._request('bcn_syncing')
        if raw:
            return res.json()
        return Sync(**res.json().get('result'))

    def getAddressTxns(self, address: str, count: int =1, token: str =None, raw=False):
        """Gets transactions for a certain address

        Parameters:
            address(str): Address to query by
            count(int): Count of transacations to return. Default: 1
            token(str1): Token to query by. Default: None
            raw(bool): Return in JSON format. Default: false

        Returns:
            txns(AddressTxns): A AddressTxns model holding txn info by address
        
        """
        params = {'address': address, 'count': count}
        if token:
            params['token'] = token
        res = self._request('bcn_transactions', [params])
        if raw:
            return res.json()
        return AddressTxns(**res.json().get('result'))

    def getPendingAddressTxns(self, address: str, raw=False):
        """Gets pending address transactions

        Parameters:
            address(str): Address to query by
            raw(bool): Return in JSON format. Default: false

        Returns:
            txns(AddressTxns): A AddressTxns model holding txn info by address
        
        """
        res = self._request('bcn_pendingTransactions', [{'address': address}])
        if raw:
            return res.json()
        return AddressTxns(**res.json().get('result'))

    def getBurntCoins(self, raw=False):
        """Gets burnt coins for your coinbase address

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            burntcoins(BurntCoins): A BurntCoins model holding burntcoin info
        
        """
        res = self._request('bcn_burntCoins')
        if raw:
            return res.json()
        return BurntCoins(**res.json().get('result'))

    def getFlipKeyword(self, index: int, raw=False):
        """Gets flip keywords by index

        Parameters:
            index(int): Index of flip keyword
            raw(bool): Return in JSON format. Default: false

        Returns:
            fkw(FlipKeyword): A FlipKeyword model holding keyword info
        
        """
        res = self._request('bcn_keyWord', [index])
        if raw:
            return res.json()
        return FlipKeyword(**res.json().get('result'))

    def getIdentities(self, raw=False):
        """Gets DNA Identities

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            identities(List[Identity]): A list of Identity models
        
        """
        res = self._request('dna_identities')
        if raw:
            return res.json()
        return [Identity(**r) for r in res.json().get('result')]

    def getIdentity(self, address: str, raw=False):
        """Gets an address' identity

        Parameters:
            address(str): Address to query by
            raw(bool): Return in JSON format. Default: false

        Returns:
            identity(Identity): Address' Identity model
        
        """
        res = self._request('dna_identity', [address])
        if raw:
            return res.json()
        return Identity(**res.json().get('result'))

    def getCurrentProcess(self, raw=False):
        """Gets flip keywords by index

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            state(State): A State model holding state information
        
        """
        res = self._request('dna_state')
        if raw:
            return res.json()
        return State(**res.json().get('result'))
    
    def getCoinbaseAddress(self, raw=False):
        """Gets coinbase address

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            addr(str): Your coinbase address
        
        """
        res = self._request('dna_getCoinbaseAddr')
        if raw:
            return res.json()
        return res.json().get('result')

    def calculateIpfsCid(self, data: str, raw=False):
        """Calculate IPFS CID

        Parameters:
            data(str): Data to calcualte IPFS CID for
            raw(bool): Return in JSON format. Default: false

        Returns:
            data(dict): CID of calculated data
        
        """
        res = self._request('ipfs_cid', [data])
        if raw:
            return res.json()
        return res.json().get('result')
    
    def addDataToIpfs(self, data: str, pin: bool = False, raw=False):
        """Add IPFS Data

        Parameters:
            data(str): Data to add to IPFS
            pin(bool): Pin to IPFS or not. Default: false
            raw(bool1): Return in JSON format. Default: false

        Returns:
            data(dict): CID of posted data
        
        """
        res = self._request('ipfs_add', [data, pin])
        if raw:
            return res.json()
        return res.json().get('result')

    def getIpfsData(self, cid: str, raw=False):
        """Gets IPFS data

        Parameters:
            cid(str): CID of IPFS data
            raw(bool): Return in JSON format. Default: false

        Returns:
            data(dict): A dictionary holding ipfs data
        
        """
        res = self._request('ipfs_get', [cid])
        if raw:
            return res.json()
        return res.json().get('result')

    def getAccounts(self, raw=False):
        """Gets your unlocked accounts

        Parameters:
            raw(bool): Return in JSON format. Default: false

        Returns:
            accounts(Accounts): An accounts model holding account data
        
        """
        res = self._request('account_list')
        if raw:
            return res.json()
        return Accounts(**res.json())
    
    def unlockAccount(self, address: str, password: str=None, time: int=None, raw=False):
        """Unlock an account

        Parameters:
            address(str): Address to unlock
            password(str1): Password of address
            time(int): Time to unlock
            raw(bool): Return in JSON format. Default: false

        Returns:
            account(str): An account string
        
        """
        params = [address]
        if password:
            params.append(password)
        if time:
            params.append(time)
        res = self._request('account_unlock', params)
        if raw:
            return res.json()
        return res.json().get('result')
    
    def addAccount(self, password: str, raw=False):
        """Add an account

        Parameters:
            password(str): Password of account
            raw(bool): Return in JSON format. Default: false

        Returns:
            account(str): An account string
        
        """
        res = self._request('account_create', [password])
        if raw:
            return res.json()
        return res.json().get('result')

    def lockAccount(self, address: str, raw=False):
        """Lock an account

        Parameters:
            address(str): Address of account
            raw(bool): Return in JSON format. Default: false

        Returns:
            account(str): An account string
        
        """
        res = self._request('account_lock', [address])
        if raw:
            return res.json()
        return res.json().get('result')

    def sendDna(self, from_: str, to: str, amount: float, max_fee: float, nonce: int = None, epoch: int = None):
        params = {
            'from': from_,
            'to': to,
            'maxFee': max_fee,
            'amount': str(amount)
        }
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_sendTransaction', [params])
        return res.json().get('result')

    def sendInvite(self, to: str, amount: int, nonce: int = None, epoch: int = None):
        params = {
            'to': to,
            'amount': amount
        }
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_sendInvite', [params])
        return res.json().get('result')
    
    def activateInvite(self, to: str, key: str = None, nonce: int = None, epoch: int = None):
        params = {
            'to': to
        }
        if key:
            params['key'] = key
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_activateInvite', [params])
        return res.json().get('result')

    def becomeOnline(self, nonce: int = None, epoch: int = None):
        params = {}
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_becomeOnline', [params])
        return res.json().get('result')

    def becomeOffline(self, nonce: int = None, epoch: int = None):
        params = {}
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_becomeOffline', [params])
        return res.json().get('result')

    def delegate(self, to: str, nonce: int = None, epoch: int = None):
        params = {
            'to': to
        }
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_delegate', [params])
        return res.json().get('result')

    def undelegate(self,nonce: int = None, epoch: int = None):
        params = {}
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_delegate', [params])
        return res.json().get('result')
    
    def killDelegator(self, to: str, nonce: int = None, epoch: int = None):
        params = {
            'to': to
        }
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_killDelegator', [params])
        return res.json().get('result')

    def changeGodAddress(self, from_: str, to: str, max_fee: float = None, nonce: int = None, epoch: int = None):
        params = {
            'from': from_,
            'to': to,
            'maxFee': max_fee,
            'type': 11
        }
        if nonce:
            params['nonce'] = nonce
        if epoch:
            params['epoch'] = epoch
        res = self._request('dna_sendTransaction', [params])
        return res.json().get('result')