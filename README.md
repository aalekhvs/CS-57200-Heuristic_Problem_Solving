# Othello Deep-Heuristic Search Engine

A hybrid adversarial search agent for Othello (Reversi) that synthesizes high-performance C++ algorithmic optimizations with a Transformer-based neural evaluation heuristic. This project resolves the trade-off between heuristic accuracy and search speed by isolating raw node generation in C++ while leveraging deep-learning patterns via a PyBind11 bridge.

## Key Features & Enhancements
1.  **Bitboard Architecture:** Utilizes 64-bit unsigned integers for game state representation, enabling hardware-level Kogge-Stone move generation and a 50x speedup over array-based models.
2.  **Zobrist-Hashed Transposition Tables:** Eliminates redundant sub-tree evaluations by caching board states, search depths, and bounds using incremental XOR hashing.
3.  **Dynamic Move Ordering:** Implements the **Killer Move Heuristic** to prioritize refutation moves, achieving a 98.7% reduction in node expansion at Depth 10.
4.  **Neural Heuristic Evaluation:** Employs a PyTorch **Multi-Head Attention** Transformer trained on expert WTHOR data to identify global spatial stability that traditional piece-counting heuristics fail to capture.

## Repository Structure
* **`src/engine/`**: High-performance C++ search core utilizing bitboards and the Alpha-Beta algorithm.
* **`src/bridge/`**: PyBind11 integration layer for cross-language data serialization and neural callbacks.
* **`src/neural/`**: PyTorch Transformer definitions, model weights, and WTHOR dataset parsers.
* **`tests/`**: Google Test (GTest) suite for validating search correctness and bitboard integrity.

## Performance Summary
| Metric | Result |
| :--- | :--- |
| **Win Rate vs. Random** | 99.7% |
| **Win Rate vs. Greedy** | 96.4% |
| **Node Reduction** | 98.7% @ Depth 10 |
| **Search Speed** | Millions of nodes/sec (C++ core) |

## Setup & Build Instructions
The project uses **CMake FetchContent** to manage dependencies automatically.

1.  **Initialize Python Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Build C++ Engine & Bindings**
    ```bash
    mkdir build && cd build
    cmake ..
    make
    ```

3.  **Run Experiments & Reproduce Results**
    To reproduce the ablation study (Experiment 2):
    ```bash
    python run_experiments.py --type ablation --depth 8
    ```
