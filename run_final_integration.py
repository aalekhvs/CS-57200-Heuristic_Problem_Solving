import sys
import torch
import numpy as np

sys.path.append('./build')
import othello_core
from src.neural.model import OthelloTransformerEval

def main():
    print("==================================================")
    print(" OTHELLO HYBRID AI: FINAL INTEGRATION RUN")
    print("==================================================\n")

    print("[1/3] Initializing C++ Bitboard Engine...")
    engine = othello_core.OthelloEngine()
    
    black_initial = 0x0000000810000000
    white_initial = 0x0000001008000000

    print("[2/3] Loading PyTorch Transformer Model...")
    model = OthelloTransformerEval(embed_dim=128, num_heads=8)
    model.eval() 

    # THE BRIDGE: This function converts C++ bitboards to PyTorch Tensors
    def neural_heuristic_callback(b, w):
        board_array = np.zeros(64, dtype=np.float32)
        
        # 1 for Black, -1 for White
        for i in range(64):
            if (b & (1 << i)):
                board_array[i] = 1.0
            elif (w & (1 << i)):
                board_array[i] = -1.0
                
        tensor_board = torch.tensor(board_array).unsqueeze(0)
        
        with torch.no_grad():
            evaluation = model(tensor_board)
            
        # Scale float evaluation to an integer for Alpha-Beta
        scaled_score = int(evaluation.item() * 100)
        return scaled_score

    print("[3/3] Executing Hybrid Search (C++ Engine + PyTorch NN)...")
    
    # Using Depth 4 to prevent the Python GIL from bottlenecking the C++ engine
    depth = 4
    print(f"-> Searching to Depth {depth}...")
    
    best_score = engine.search_enhanced(
        b=black_initial, 
        w=white_initial, 
        depth=depth, 
        alpha=-100000, 
        beta=100000, 
        isBlack=True, 
        ply=0, 
        hash=0,
        nnEval=neural_heuristic_callback # Passing the Python function to C++
    )

    print("\n==================================================")
    print(f"🎉 SUCCESS! Final Evaluated Score: {best_score}")
    print("The C++ Engine successfully queried the PyTorch model at the leaf nodes!")
    print("==================================================")

if __name__ == "__main__":
    main()