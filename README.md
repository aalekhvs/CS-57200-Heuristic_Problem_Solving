# Othello Deep-Heuristic Search Engine

A hybrid adversarial search agent for Othello (Reversi) that synthesizes high-performance C++ search optimizations with a Transformer-based neural evaluation heuristic.

## Implemented Enhancements
This project implements the following search and heuristic enhancements over a standard Minimax baseline:
1. **Zobrist-Hashed Transposition Tables:** Eliminates redundant sub-tree evaluation by caching previously computed board states and best moves using ultra-fast 64-bit XOR keys.
2. **Dynamic Move Ordering (Killer Heuristic):** Prioritizes moves that previously triggered Beta-cutoffs at the same search ply, maximizing the efficiency of Alpha-Beta pruning.
3. **Neural Heuristic Evaluation:** Replaces rigid, hand-crafted static evaluations with a PyTorch Multi-Head Attention network trained on WTHOR expert game data to capture complex, long-range spatial dependencies.

## Architecture
- **`src/engine/`**: Core C++ implementation utilizing 64-bit bitboards for maximum memory efficiency and CPU throughput.
- **`src/python_bindings/`**: PyBind11 integration layer exposing the high-speed C++ search tree to the Python environment.
- **`src/neural/`**: PyTorch implementation of the Multi-Head Attention evaluation model and WTHOR binary parsers.
- **`tests/`**: GTest suite for validating game logic, Minimax mathematical correctness, and Zobrist hash integrity.

## System Requirements
- CMake (>= 3.12)
- C++17 compliant compiler (GCC/Clang)
- Python 3.8+

## Setup & Build Instructions

1. **Initialize the Python Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt