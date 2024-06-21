import os
from seleniumbase import SB
import Xlib.display
from sbvirtualdisplay.display import Display

print("DISPLAY" in os.environ.keys())
disp = Display(
    visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
)
disp.start()
print("DISPLAY" in os.environ.keys())
print(os.environ['DISPLAY'])
import pyautogui  # noqa
print(pyautogui._pyautogui_x11._display)
pyautogui._pyautogui_x11._display = (
    Xlib.display.Display(os.environ['DISPLAY'])
)
print(pyautogui._pyautogui_x11._display)
print(os.environ['DISPLAY'])

with SB(uc=True, test=True, rtf=True, headed=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(4)
    pyautogui.press("\t")
    sb.sleep(0.1)
    pyautogui.press(" ")
    sb.sleep(2)
    sb.connect()
    sb.assert_text("Welcome to Middle Earth!", "h1")
    print(sb.get_text("h1"))

with SB(uc=True, test=True, rtf=True, headed=True) as sb:
    url = "https://seleniumbase.io/apps/brotector"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(4)
    pyautogui.press("\t")
    sb.sleep(0.1)
    pyautogui.press(" ")
    sb.sleep(2)
    sb.connect()
    sb.assert_text("SUCCESS", "#pText")
