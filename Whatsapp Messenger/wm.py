# Importing necessary libraries
import pyautogui as pg  # For automating keyboard and mouse actions
import time  # For introducing delays in the script

# Displaying a message before starting WhatsApp Messenger
print("WhatsApp Messenger will run after 10 seconds")

# Introducing a delay of 10 seconds before running WhatsApp
time.sleep(10)

# Displaying a message indicating that WhatsApp Messenger is running
print("WhatsApp Messenger is running")

# Loop to send test messages three times
for i in range(3):
    # Typing the test message
    pg.typewrite("Hello, this is a test message\n")
    # Introducing a short delay before pressing Enter
    time.sleep(0.5)
    # Pressing Enter to send the message
    pg.press("Enter")
