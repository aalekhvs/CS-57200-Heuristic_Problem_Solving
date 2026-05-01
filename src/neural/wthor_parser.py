import struct
import numpy as np

def parse_wthor_file(file_path):
    """
    Parses expert game data from WTHOR binary files.
    """
    games = []
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            # 16-byte header, 68-byte game entries
            for i in range(16, len(data), 68):
                move_data = data[i+8 : i+68]
                games.append(list(move_data))
        return np.array(games)
    except FileNotFoundError:
        # Fixed: Passed an empty list to np.array()
        return np.array([])