import pyautogui, time

time.sleep(5)

spam_list = open("spamwords.txt", "r")

for word in spam_list:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
