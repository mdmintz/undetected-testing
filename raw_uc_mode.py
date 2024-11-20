"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB


with SB(uc=True, test=True, rtf=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.uc_gui_press_keys("\t ")
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    url = "https://www.virtualmanager.com/en/login"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.uc_gui_click_captcha()
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
