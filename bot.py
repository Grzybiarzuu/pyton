import pyautogui
import time
import random
import string

def generate_random():
            digit_char = random.choices(string.ascii_lowercase, k=9) + random.choices(string.digits, k=2)
            random.shuffle(digit_char)
            return ''.join(digit_char)

i = 0
time.sleep(3)
while i < 420:
    a = generate_random()
    a = a + "@gmail.com"
    pyautogui.press('tab', presses = 3)
    pyautogui.write(a)
    pyautogui.press('tab')
    if i % 2 == 0:
        pyautogui.write('Amongus party')
    if i % 2 == 1:
        pyautogui.write('Sussy party')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)
    if i % 5 == 0:
        print (i)
    i = i + 1