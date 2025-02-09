import pyautogui
import time

def jiggle_mouse():
    while True:
        x, y = pyautogui.position()  # Get current mouse position
        pyautogui.moveTo(x + 3, y + 1)  # Move slightly
        time.sleep(0.1)
        pyautogui.moveTo(x, y)  # Move back
        time.sleep(2)  # Wait for 2 seconds

if __name__ == "__main__":
    jiggle_mouse()