import sys
import time
import torch
import numpy as np

sys.path.append('./build')
import othello_core
from src.neural.model import OthelloTransformerEval

def main():
    print("==================================================")
    print(" OTHELLO AI TOURNAMENT & BENCHMARK SUITE")
    print("==================================================\n")

    # 1. Initialize Engines and Models
    engine = othello_core.OthelloEngine()
    
    print("Loading PyTorch Neural Heuristic...")
    model = OthelloTransformerEval(embed_dim=128, num_heads=8)
    model.eval()

    def neural_heuristic_callback(b, w):
        board_array = np.zeros(64, dtype=np.float32)
        for i in range(64):
            if (b & (1 << i)): board_array[i] = 1.0
            elif (w & (1 << i)): board_array[i] = -1.0
        tensor_board = torch.tensor(board_array).unsqueeze(0)
        with torch.no_grad():
            evaluation = model(tensor_board)
        return int(evaluation.item() * 100)

    # 2. Define Benchmark Board States
    # Starting Position
    b_start = 0x0000000810000000
    w_start = 0x0000001008000000

    # Complex Mid-Game Position
    b_mid = 0x00003C1810080000
    w_mid = 0x0000002428100000

    scenarios = [
        ("Early Game (Turn 1)", b_start, w_start, 6), # Depth 6 for speed
        ("Complex Mid-Game", b_mid, w_mid, 6)
    ]

    print("\nStarting Evaluation Benchmark...\n")
    print(f"{'Scenario':<25} | {'Algorithm':<20} | {'Time (sec)':<12} | {'Score'}")
    print("-" * 75)

    for name, b, w, depth in scenarios:
        # --- TEST 1: BASELINE MINIMAX ---
        start_time = time.time()
        score_base = engine.search_baseline(b, w, depth, -100000, 100000, True)
        time_base = time.time() - start_time
        print(f"{name:<25} | {'Baseline Minimax':<20} | {time_base:<12.4f} | {score_base}")

        # --- TEST 2: ENHANCED (TT + KILLER MOVES) ---
        start_time = time.time()
        score_enh = engine.search_enhanced(b, w, depth, -100000, 100000, True, 0, 0, None)
        time_enh = time.time() - start_time
        print(f"{'':<25} | {'Enhanced (TT+Killer)':<20} | {time_enh:<12.4f} | {score_enh}")

        # --- TEST 3: HYBRID NEURAL ---
        # Note: We lower the depth slightly for the neural net to simulate batched limits
        nn_depth = depth - 2 
        start_time = time.time()
        score_hyb = engine.search_enhanced(b, w, nn_depth, -100000, 100000, True, 0, 0, neural_heuristic_callback)
        time_hyb = time.time() - start_time
        print(f"{'':<25} | {f'Hybrid Neural (D{nn_depth})':<20} | {time_hyb:<12.4f} | {score_hyb}")
        print("-" * 75)

    print("\n✅ Benchmark Complete. Use these times for your Final Report graphs!")

if __name__ == "__main__":
    main()