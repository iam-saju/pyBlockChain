# pyBasicBC - Basic Blockchain Implementation in Python

A simple and educational blockchain implementation in Python that demonstrates core blockchain concepts including blocks, chains, proof-of-work mining, and cryptographic hashing.

## 🚀 Features

- **Block Structure**: Each block contains data, hash, nonce, and previous block hash
- **Proof of Work**: Mining algorithm with adjustable difficulty
- **Chain Management**: Maintains a linked chain of blocks
- **Transaction Pool**: Simple transaction pool for pending data
- **Cryptographic Hashing**: SHA-256 hashing for block integrity

## 📁 Project Structure

```
pyBasicBC/
├── block.py          # Block class implementation
├── chain.py          # Blockchain chain management
├── main.py           # Main execution script
├── playground.py     # Experimental code and examples
├── env/              # Virtual environment
└── README.md         # This file
```

## 🛠️ Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd pyBasicBC
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   ```
   
   Note: This project uses only Python standard library modules (`hashlib`), so no additional packages are required.

## 🎯 Usage

### Basic Usage

Run the main script to see the blockchain in action:

```bash
python main.py
```

This will:
- Create a blockchain with difficulty level 20
- Add 6 transactions to the pool (0-5)
- Mine each transaction into a block
- Display block details including hash, previous hash, nonce, and data

### Example Output

```
hash : 		0000000000000000000000000000000000000000000000000000000000000000
previous hash : 		0000000000000000000000000000000000000000000000000000000000000000
nonce :		0
data :		origin

 ========== 

hash : 		0000000000000000000000000000000000000000000000000000000000000000
previous hash : 		0000000000000000000000000000000000000000000000000000000000000000
nonce :		504
data :		0

 ========== 
```

### Custom Usage

You can create your own blockchain instance:

```python
from chain import chain

# Create a blockchain with difficulty 16
my_blockchain = chain(16)

# Add some data to the transaction pool
my_blockchain.add_to_pool("Hello, Blockchain!")
my_blockchain.add_to_pool("Another transaction")

# Mine the transactions
my_blockchain.mine()
my_blockchain.mine()
```

## 🔧 Core Components

### Block Class (`block.py`)

Represents a single block in the blockchain:

- **Attributes:**
  - `data`: The data stored in the block
  - `hash`: The block's hash value
  - `nonce`: Number used in mining
  - `prev_hash`: Hash of the previous block

- **Methods:**
  - `mine(difficulty)`: Performs proof-of-work mining

### Chain Class (`chain.py`)

Manages the blockchain:

- **Attributes:**
  - `difficulty`: Mining difficulty level
  - `blocks`: List of all blocks in the chain
  - `pool`: Transaction pool for pending data

- **Methods:**
  - `add_to_pool(data)`: Add data to transaction pool
  - `mine()`: Mine a block from the pool
  - `proof_of_work(block)`: Verify block's proof of work
  - `add_to_chain(block)`: Add verified block to chain

## 🔍 Understanding the Code

### Proof of Work Algorithm

The mining algorithm works by:
1. Combining block data, nonce, and previous hash
2. Computing SHA-256 hash
3. Checking if the hash meets the difficulty requirement
4. Incrementing nonce and repeating until successful

### Difficulty Adjustment

The difficulty parameter controls how hard it is to mine a block:
- Higher difficulty = more leading zeros required in hash
- Lower difficulty = easier to find valid hash

## 🧪 Playground

The `playground.py` file contains experimental code including:
- Linked list node implementation
- Hash function examples
- Mining difficulty demonstrations

## 📚 Learning Objectives

This project demonstrates:
- Blockchain data structures
- Cryptographic hashing
- Proof-of-work consensus
- Chain validation
- Mining algorithms

## 🤝 Contributing

Feel free to experiment with the code:
- Try different difficulty levels
- Add new features like block validation
- Implement additional consensus mechanisms
- Add transaction signing

## 📄 License

This is an educational project. Feel free to use and modify for learning purposes.

## 🔗 Related Concepts

- **Blockchain**: Distributed ledger technology
- **Cryptocurrency**: Digital currencies like Bitcoin
- **Smart Contracts**: Self-executing contracts
- **Decentralization**: Distributed network architecture

---

*Happy coding and learning! 🚀*
