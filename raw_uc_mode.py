from seleniumbase import SB
from sbvirtualdisplay import Display
import os

display = Display(
    visible=True, size=(1920, 1080), backend="xvfb", use_xauth=True
)
display.start()
os.environ["DISPLAY"] = f":{display.display}"
with SB(uc=True, headed=True) as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.uc_open_with_reconnect(url, 10)
    sb.uc_gui_click_captcha()
    sb.sleep(5)
    print(sb.get_page_title())
display.stop()
