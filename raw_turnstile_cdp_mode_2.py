from pyvirtualdisplay import Display
from seleniumbase import SB

display = Display(visible=1, size=(1600, 900))
display.start()

with SB(uc=True, test=True, headed=True) as sb:
    url = "https://seleniumbase.io/apps/turnstile"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.assert_element("img#captcha-success", timeout=3)
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=3)
    sb.save_screenshot_to_logs()

display.stop()
