import asyncio
from web3 import Web3

# Centralized Infura API key
INFURA_API_KEY = ""

# Dictionary containing RPC URLs for various mainnets and testnets
# Users should replace YOUR_INFURA_API_KEY with their own Infura API key
NETWORKS = {
    "Mainnets": {
        "Ethereum Mainnet": f"https://mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Polygon Mainnet": f"https://polygon-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Base Mainnet": f"https://base-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Optimism Mainnet": f"https://optimism-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Arbitrum Mainnet": f"https://arbitrum-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Avalanche C-Chain Mainnet": f"https://avalanche-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Celo Mainnet": f"https://celo-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "ZKsync Mainnet": f"https://zksync-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "BSC Mainnet": f"https://bsc-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Mantle Mainnet": f"https://mantle-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "opBNB Mainnet": f"https://opbnb-mainnet.infura.io/v3/{INFURA_API_KEY}",
        "Scroll Mainnet": f"https://scroll-mainnet.infura.io/v3/{INFURA_API_KEY}",
    },
    "Testnets": {
        "Ethereum Sepolia": f"https://sepolia.infura.io/v3/{INFURA_API_KEY}",
        "Polygon Amoy": f"https://polygon-amoy.infura.io/v3/{INFURA_API_KEY}",
        "Base Sepolia": f"https://base-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "Blast Sepolia": f"https://blast-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "Optimism Sepolia": f"https://optimism-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "Arbitrum Sepolia": f"https://arbitrum-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "Palm Testnet": f"https://palm-testnet.infura.io/v3/{INFURA_API_KEY}",
        "Avalanche C-Chain Fuji": f"https://avalanche-fuji.infura.io/v3/{INFURA_API_KEY}",
        "Starknet Sepolia": f"https://starknet-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "Celo Alfajores": f"https://celo-alfajores.infura.io/v3/{INFURA_API_KEY}",
        "ZKsync Sepolia": f"https://zksync-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "BSC Testnet": f"https://bsc-testnet.infura.io/v3/{INFURA_API_KEY}",
        "Mantle Sepolia": f"https://mantle-sepolia.infura.io/v3/{INFURA_API_KEY}",
        "opBNB Testnet": f"https://opbnb-testnet.infura.io/v3/{INFURA_API_KEY}",
        "Scroll Sepolia": f"https://scroll-sepolia.infura.io/v3/{INFURA_API_KEY}",
    },
}


async def check_transaction_in_network(hash_input, network_name, rpc_url):
    """
    Check if a transaction exists in a specific blockchain network.

    Args:
        hash_input (str): The transaction hash to check.
        network_name (str): The name of the blockchain network.
        rpc_url (str): The RPC URL of the blockchain network.

    Returns:
        str: The name of the network if the transaction is found, otherwise None.
    """
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if web3.is_connected():
            transaction = web3.eth.get_transaction(hash_input)
            if transaction:
                print(f"Transaction found in {network_name}")
                return network_name
    except Exception:
        pass
    return None


async def detect_blockchain(hash_input):
    """
    Detect which blockchain a transaction belongs to by checking multiple networks.

    Args:
        hash_input (str): The transaction hash to check.

    Returns:
        str: The name of the blockchain network where the transaction was found,
             or "Unknown Blockchain" if not found.
    """
    for category, networks in NETWORKS.items():
        tasks = []
        for name, url in networks.items():
            task = asyncio.create_task(check_transaction_in_network(hash_input, name, url))
            tasks.append(task)
        for task in asyncio.as_completed(tasks):
            result = await task
            if result:
                return result
        if category == "Mainnets":
            print("Transaction not found in any Mainnet. Checking Testnets...")
    print("Transaction not found in any blockchain.")
    return "Unknown Blockchain"


if __name__ == "__main__":
    # Prompt the user to input a transaction hash
    hash_input = input("Enter a hash: ").strip()
    
    # Validate the hash format
    if not hash_input.startswith("0x") or len(hash_input) != 66:
        print("Invalid hash format. Transaction hashes should start with '0x' and have 64 characters.")
    else:
        # Run the blockchain detection process
        result = asyncio.run(detect_blockchain(hash_input))
        print(f"Result: {result}")
