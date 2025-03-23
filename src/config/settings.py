import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Directory for temporary files
TEMP_DIR = os.path.join(BASE_DIR, 'data', 'temp')

# Directory for output files
OUTPUT_DIR = os.path.join(BASE_DIR, 'data', 'output')

# Maximum upload size (in MB)
MAX_UPLOAD_SIZE = 200

# Create directories if they don't exist
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True) 