"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB

with SB(uc=True, test=True, rtf=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.uc_open_with_disconnect(url, 2)
    sb.uc_gui_press_keys("\t ")
    sb.reconnect(2)
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    url = "https://www.virtualmanager.com/en/login"
    sb.uc_open_with_reconnect(url, 4)
    print(sb.get_page_title())
    sb.uc_gui_click_cf(retry=True)
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
