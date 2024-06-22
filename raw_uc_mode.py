"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB

print("DISPLAY" in os.environ.keys())
if "DISPLAY" in os.environ.keys():
    print(os.environ['DISPLAY'])
print(pyautogui._pyautogui_x11._display)

with SB(uc=True, test=True, rtf=True, xvfb=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.uc_open_with_disconnect(url, 2)
    sb.uc_gui_press_keys("\t ")
    sb.reconnect(2)
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
