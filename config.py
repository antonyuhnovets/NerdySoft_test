import os

# Get current dir and define output catalog
CURRENT_DIR = os.path.abspath(os.getcwd())
OUTPUT_DIR = f'{CURRENT_DIR}\output'

# Data lists for vocabulary
VOCABULARY = ['one', 'two', 'three', 'four', 'five']
LARGE_DATA_LOCATION = f'{CURRENT_DIR}\sample_data.txt'
VOCABULARY_LARGE = open(LARGE_DATA_LOCATION).read().split()

