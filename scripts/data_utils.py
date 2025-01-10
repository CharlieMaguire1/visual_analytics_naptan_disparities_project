import pandas as pd

# Loading datasets
def load_csv(file_path, low_memory = False):
    return pd.read_csv(file_path, low_memory = low_memory)

# Cleaning 