import struct
import numpy as np

def parse_wthor_file(file_path):
    """
    Parses binary WTHOR.wtb files into move sequences and scores.
    This provides the expert-level training data for the Transformer-based evaluation model .
    """
    games = []
    
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            # WTHOR format: 16-byte header, followed by 68-byte game blocks [1, 2]
            # Each 68-byte block: 8 bytes for game info, 60 bytes for moves
            for i in range(16, len(data), 68):
                # Slice the move data (indices 8 through 68 of the block)
                move_data = data[i+8 : i+68]
                games.append(list(move_data))
                
        return np.array(games)
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return np.array()