from seleniumbase import SB

with SB(uc=True, guest=True, ad_block=True, use_chromium=True) as sb:
    url = "https://serienstream.to/serie/24/staffel-1/episode-1"
    sb.activate_cdp_mode(url)
    sb.sleep(4)
    sb.solve_captcha()
    sb.sleep(3)
    sb.save_screenshot_to_logs()
