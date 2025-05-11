from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Check connection
if not w3.is_connected():
    raise Exception("Web3 not connected. Start Ganache!")

# Contract Address and ABI (paste your address and ABI here)
contract_address = "0xEf9f1ACE83dfbB8f559Da621f4aEA72C6EB10eBf"

abi = [
    {
        "inputs": [{"internalType": "string", "name": "docHash", "type": "string"}],
        "name": "submitDocument",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "docHash", "type": "string"}],
        "name": "checkDocument",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "", "type": "string"}],
        "name": "submittedHashes",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# Create Contract Instance
contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]

def add_record(document_hash, is_plagiarized):
    try:
        tx_hash = contract.functions.submitDocument(document_hash).transact({
            'from': account
        })
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Document {document_hash} submitted to Blockchain!")
        return tx_hash.hex()
    except Exception as e:
        print(f"Blockchain Error: {e}")
        return None
