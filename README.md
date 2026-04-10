# Othello Deep-Heuristic Search Engine

## Repository Structure
- `/src/engine/`: Optimized C++ core (Bitboards, Zobrist TT, Killer Heuristic).
- `/src/python_bindings/`: PyBind11 integration code.
- `/src/neural/`: PyTorch Transformer model and WTHOR data parsing.
- `/tests/`: GTest suite for validating minimax correctness.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Build the C++ core:
   ```bash
   mkdir build && cd build
   cmake..
   make

Running Experiments
To run the performance comparison between the Baseline and Enhanced algorithms:
python src/neural/run_comparison.py