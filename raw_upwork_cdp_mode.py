from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://www.upwork.com/nx/search/jobs/"
    sb.activate_cdp_mode(url)
    sb.sleep(3)
    sb.uc_gui_click_captcha()
    sb.sleep(1)
    sb.press_keys('input[type="search"]', "WordPress\n")
    sb.sleep(2)
    print(sb.get_text('[data-test="JobsList"]'))
