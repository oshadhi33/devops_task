import os
import logging

# Set log directory
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure log directory exists

# Configure logging
log_filename = os.path.join(LOG_DIR, "file_processing.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def count_lines(file_path):
    """Counts total lines and non-empty lines in a file."""
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()
            total_lines = len(lines)
            non_empty_lines = sum(1 for line in lines if line.strip())  # Ignore blank lines
        
        log_message = (
            f"Processed file: {file_path} | Total lines: {total_lines} | Non-empty lines: {non_empty_lines}"
        )
        logging.info(log_message)
        print(log_message)
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    INPUT_DIR = "/app/input_files"
    
    # Process the first file in the directory (Docker-compatible)
    files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
    
    if not files:
        print("No files found in input directory.")
        logging.warning("No files found in input directory.")
    else:
        file_path = os.path.join(INPUT_DIR, files[0])  # Process the first file
        count_lines(file_path)
