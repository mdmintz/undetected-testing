import os
from seleniumbase import SB

agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
    "Safari/537.36"
)

with SB(uc=True, test=True, agent=agent) as sb:
    import pyautogui
    import Xlib.display
    from sbvirtualdisplay.display import Display
    disp = Display(
        visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
    )
    disp.start()
    pyautogui._pyautogui_x11._display = (
        Xlib.display.Display(os.environ['DISPLAY'])
    )

    url = "https://seleniumbase.io/hobbit/login"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(3)
    pyautogui.press("\t")
    pyautogui.press(" ")
    sb.sleep(3)
    sb.connect()
    sb.assert_text("Welcome to Middle Earth!", "h1")
    print(sb.get_text("h1"))


with SB(uc=True, test=True, agent=agent) as sb:
    import pyautogui
    import Xlib.display
    from sbvirtualdisplay.display import Display
    disp = Display(
        visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
    )
    disp.start()
    pyautogui._pyautogui_x11._display = (
        Xlib.display.Display(os.environ['DISPLAY'])
    )
    url = "https://seleniumbase.io/apps/brotector"
    sb.uc_open_with_reconnect(url, 3)
    print(sb.get_text("html"))

with SB(uc=True, test=True, agent=agent) as sb:
    import pyautogui
    import Xlib.display
    from sbvirtualdisplay.display import Display
    disp = Display(
        visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
    )
    disp.start()
    pyautogui._pyautogui_x11._display = (
        Xlib.display.Display(os.environ['DISPLAY'])
    )
    url = "https://seleniumbase.io/apps/brotector"
    sb.driver.uc_open_with_disconnect(url)
    sb.sleep(3)
    pyautogui.press("\t")
    pyautogui.press(" ")
    sb.sleep(3)
    sb.connect()
    print(sb.get_text("html"))

with SB(uc=True, test=True, agent=agent) as sb:
    import pyautogui
    import Xlib.display
    from sbvirtualdisplay.display import Display
    disp = Display(
        visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
    )
    disp.start()
    pyautogui._pyautogui_x11._display = (
        Xlib.display.Display(os.environ['DISPLAY'])
    )
    url = "https://user-agent-client-hints.glitch.me/"
    sb.uc_open_with_reconnect(url, 3)
    print(sb.get_text("html"))

with SB(test=True) as sb:
    url = "https://user-agent-client-hints.glitch.me/"
    sb.open(url)
    print(sb.get_text("html"))
