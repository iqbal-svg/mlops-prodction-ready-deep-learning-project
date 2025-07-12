import os       # Import the OS module to handle directory and file paths
import sys      # Import sys module to stream logs to the console (stdout)
import logging  # Import Python’s built-in logging module for logging functionality

# Define the format of log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# → Includes: timestamp, log level (INFO/ERROR etc.), module name, and the message

# Create a folder name for storing logs
log_dir = "logs"  # Folder to store log files

# Create full path for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")  
# → This will be 'logs/running_logs.log'

# Make the log directory if it doesn’t exist
os.makedirs(log_dir, exist_ok=True)  
# → Creates 'logs' directory if not already present, no error if it exists

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,              # Log messages at INFO level and above (INFO, WARNING, ERROR)
    format=logging_str,              # Use the log format defined above
    handlers=[                       # Define where to send the logs
        logging.FileHandler(log_filepath),    # Save logs to file
        logging.StreamHandler(sys.stdout)     # Also print logs to the terminal
    ]
)

# Create a logger instance with a custom name
logger = logging.getLogger("cnnClassifierLogger")  
# → Use this logger throughout your code to log messages