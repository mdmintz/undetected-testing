import os
from seleniumbase import SB

with SB(uc=True, test=True, xvfb=True) as sb:
    os.environ["DISPLAY"] = ":0"
    import pyautogui
    url = "https://seleniumbase.io/hobbit/login"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(3)
    pyautogui.press("\t")
    pyautogui.press(" ")
    sb.sleep(3)
    sb.connect()
    sb.assert_text("Welcome to Middle Earth!", "h1")
    print(sb.get_text("h1"))
