from seleniumbase import SB

with SB(
    uc=True, test=True, xvfb=True, xvfb_metrics="1920,1080", headed=True
) as sb:
    url = "https://seleniumbase.io/apps/turnstile"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    import pyautogui
    print(pyautogui.size())
