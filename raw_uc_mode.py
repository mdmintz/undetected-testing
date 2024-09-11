"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB
from seleniumbase import config as sb_config

with SB(uc=True, test=True, rtf=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.uc_open_with_disconnect(url, 3)
    sb.uc_gui_press_keys("\t ")
    sb.reconnect(3)
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    import pyautogui
    url = "https://www.virtualmanager.com/en/login"
    sb.uc_open_with_reconnect(url, 4)
    sb.uc_gui_click_captcha()
    print(sb.get_page_title())
    if (
        "Just a moment" in sb.get_page_title()
        and hasattr(sb_config, "_saved_cf_x_y")
    ):
        sb.uc_open_with_disconnect(url)
        sb.sleep(4)
        pyautogui.click(sb_config._saved_cf_x_y)
        sb.sleep(3)
        sb.reconnect()
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
