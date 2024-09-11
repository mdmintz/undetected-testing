from seleniumbase import SB

with SB(uc=True, xvfb=True) as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.uc_open_with_reconnect(url, 10)
    sb.uc_gui_click_captcha()
    sb.sleep(5)
    print(sb.get_page_title())
