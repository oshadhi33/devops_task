import os
import sys
import logging
from datetime import datetime

# Setup logging
log_file = "/app/logs/file_processing.log"
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

def count_lines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            line_count = sum(1 for _ in f)
        logging.info(f"Processed file: {file_path} | Total lines: {line_count}")
        print(f"Processed file: {file_path} | Total lines: {line_count}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = "/app/input_files/sample.txt"  # Default file path inside the container
    if os.path.exists(file_path):
        count_lines(file_path)
    else:
        print(f"Error: File '{file_path}' not found.")
        logging.error(f"File '{file_path}' not found.")
