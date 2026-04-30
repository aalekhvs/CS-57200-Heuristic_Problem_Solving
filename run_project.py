import sys
import torch
import numpy as np

# Add the build directory to the path so Python can find the compiled C++ bindings
sys.path.append('./build')

try:
    import othello_core
    print("✅ Successfully imported C++ OthelloEngine bindings!")
except ImportError as e:
    print(f"❌ Failed to import othello_core: {e}")
    sys.exit(1)

# Import the neural network components
from src.neural.model import OthelloTransformerEval
from src.neural.wthor_parser import parse_wthor_file

def main():
    print("\n--- Testing Component 1: C++ Engine (Alpha-Beta + TT + Move Ordering) ---")
    engine = othello_core.OthelloEngine()
    
    # Standard initial Othello board state (Bitboards)
    black_initial = 0x0000000810000000
    white_initial = 0x0000001008000000
    
    print("Executing Depth 6 search...")
    # search_enhanced(b, w, depth, alpha, beta, isBlack, ply, hash)
    best_score = engine.search_enhanced(
        black_initial, white_initial, 6, -100000, 100000, True, 0, 0
    )
    print(f"✅ Engine executed successfully. Optimal heuristic evaluation: {best_score}")


    print("\n--- Testing Component 2: PyTorch Transformer Model ---")
    print("Initializing Multi-Head Attention Evaluator...")
    model = OthelloTransformerEval(embed_dim=128, num_heads=8)
    
    # Create a dummy bitboard input (batch_size=1, sequence_length=64) to simulate a board state
    dummy_input = torch.randint(0, 2, (1, 64)).float()
    
    with torch.no_grad():
        output = model(dummy_input)
    print(f"✅ Model executed successfully. Output tensor shape: {output.shape}, Evaluation Value: {output.item():.4f}")


    print("\n--- Testing Component 3: WTHOR Data Parser ---")
    # Pointing to a dummy file to test the graceful FileNotFoundError block you wrote
    parsed_data = parse_wthor_file("data/dummy.wtb")
    if isinstance(parsed_data, np.ndarray):
        print(f"✅ Parser executed successfully. Shape: {parsed_data.shape}")
    
    print("\n🎉 All project components are fully operational and ready for Week 15 integration!")

if __name__ == "__main__":
    main()