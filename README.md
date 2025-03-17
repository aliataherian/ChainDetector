# ChainDetector


## Overview
This script detects the blockchain network to which a given transaction hash belongs by checking multiple blockchain networks via their RPC endpoints.

## Features
- Supports both **Mainnets** and **Testnets**.
- Utilizes **Infura API** for connecting to various blockchain networks.
- Uses **asyncio** for concurrent execution, speeding up the detection process.

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Required dependencies:
  ```sh
  pip install web3 asyncio
  ```
- An **Infura API Key** (sign up at [Infura](https://infura.io/) to get one).

## Setup

1. **Obtain an Infura API Key**:
   - Go to [Infura's website](https://infura.io/).
   - Create an account (if you don’t have one).
   - Create a new project and get your API key.
   - Replace `INFURA_API_KEY` in the script with your own key.

2. **Run the script**:
   ```sh
   python ChainDetector.py
   ```
   - Enter a transaction hash when prompted.
   - The script will determine which blockchain the transaction belongs to.

## Supported Networks
The script checks for the transaction in the following **Mainnets** and **Testnets**:

### Mainnets:
- Ethereum
- Polygon
- Base
- Optimism
- Arbitrum
- Avalanche C-Chain
- Celo
- ZKsync
- BSC
- Mantle
- opBNB
- Scroll

### Testnets:
- Ethereum Sepolia
- Polygon Amoy
- Base Sepolia
- Blast Sepolia
- Optimism Sepolia
- Arbitrum Sepolia
- Palm Testnet
- Avalanche Fuji
- Starknet Sepolia
- Celo Alfajores
- ZKsync Sepolia
- BSC Testnet
- Mantle Sepolia
- opBNB Testnet
- Scroll Sepolia

## Example Output
```
Enter a hash: 0x123456789abcdef...
Transaction found in Ethereum Mainnet
Result: Ethereum Mainnet
```
If the transaction is not found in any mainnet, the script will proceed to check testnets.

## Notes
- Ensure your **Infura API key** is valid and correctly set in the script.
- Some testnets may not have your transaction if it belongs to a different chain.
- If the transaction is not found, the output will be `Unknown Blockchain`.

## License
This project is licensed under the MIT License.

