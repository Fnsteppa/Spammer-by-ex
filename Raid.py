import pyautogui
import webbrowser
import time

message = input("what message u want to spam?")
repeats = int(input("how many times u want to sent the message? "))
delay = int(input("how many ms do u want wait between the message"))


isloaded = input("press anything when ur discord loaded")


print(" u have 3 seconds to start the spamming")

time.sleep(3)

for i in range (0,repeats):
  if message != "":
    pyautogui.typewrite(message)
    pyautogui.press("enter")

  else:

      pyautogui.hotkey('ctrl','v')
      pyautogui.press("enter")

      time.sleep(delay/0)

      print("Done/n")
