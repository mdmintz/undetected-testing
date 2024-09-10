"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    import pyautogui
    url = "https://www.virtualmanager.com/en/login"
    sb.uc_open_with_reconnect(url, 6)
    sb.disconnect()
    pyautogui.moveTo(228, 387, 1.05, pyautogui.easeOutQuad)
    sb.sleep(0.056)
    pyautogui.click()
    sb.sleep(3)
    sb.reconnect()
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
