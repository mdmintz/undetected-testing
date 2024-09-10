import nodriver
import time
import os
from sbvirtualdisplay.display import Display
import pyautogui
import Xlib.display


async def main():
    disp = Display(
        visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
    )
    disp.start()
    browser = await nodriver.start()
    page = await browser.get("https://www.virtualmanager.com/en/login")
    pyautogui._pyautogui_x11._display = (
        Xlib.display.Display(os.environ['DISPLAY'])
    )
    print(await page.evaluate("document.title"))
    time.sleep(3)
    pyautogui.click(228, 387)
    time.sleep(3)
    print(await page.evaluate("document.title"))
    disp.stop()

if __name__ == "__main__":
    nodriver.loop().run_until_complete(main())
