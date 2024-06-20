from seleniumbase import SB

with SB(uc=True, test=True) as sb:
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
