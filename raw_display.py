import pyautogui
from seleniumbase import SB

with SB(uc=True, test=True, xvfb_metrics="1920,1080") as sb:
    url = "https://seleniumbase.io/demo_page"
    sb.activate_cdp_mode(url)
    print(pyautogui.size())
