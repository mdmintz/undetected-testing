import os
from seleniumbase import SB
import Xlib.display
from sbvirtualdisplay.display import Display

disp = Display(
    visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
)
disp.start()
import pyautogui  # noqa
pyautogui._pyautogui_x11._display = (
    Xlib.display.Display(os.environ['DISPLAY'])
)

with SB(uc=True, test=True, rtf=True, headed=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(2.5)
    pyautogui.press("\t")
    pyautogui.press(" ")
    sb.sleep(2.5)
    sb.connect()
    sb.assert_text("Welcome to Middle Earth!", "h1")
    print(sb.get_text("h1"))

with SB(uc=True, test=True, rtf=True, headed=True) as sb:
    url = "https://seleniumbase.io/apps/brotector"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(2.5)
    pyautogui.press("\t")
    pyautogui.press(" ")
    sb.sleep(2.5)
    sb.connect()
    sb.assert_text("SUCCESS", "#pText")
