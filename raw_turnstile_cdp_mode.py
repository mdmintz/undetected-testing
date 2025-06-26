from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://seleniumbase.io/apps/turnstile"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.uc_gui_click_captcha()
    sb.cdp.gui_click_element("div.cf-turnstile")
    sb.cdp.gui_click_x_y(124.0, 323.15625)
    sb.assert_element("img#captcha-success", timeout=3)
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=3)
    sb.save_screenshot_to_logs()
