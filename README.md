# pyBasicBC

A minimal blockchain implementation in Python demonstrating core concepts with clean, educational code.

## Features

- 🔗 **Blockchain Structure** - Linked blocks with cryptographic hashing
- ⛏️ **Proof of Work** - Adjustable difficulty mining algorithm  
- 📦 **Transaction Pool** - Simple pending transaction management
- 🔒 **SHA-256 Hashing** - Cryptographic integrity verification

## Quick Start

```bash
# Run the blockchain demo
python main.py
```

## Usage

```python
from chain import chain

# Create blockchain with difficulty 16
bc = chain(16)

# Add transactions and mine
bc.add_to_pool("Hello, Blockchain!")
bc.mine()
```

## Project Structure

```
pyBasicBC/
├── block.py       # Block implementation
├── chain.py       # Blockchain logic  
├── main.py        # Demo script
└── playground.py  # Experiments
```

## License

MIT License - see [LICENSE](LICENSE) for details.

