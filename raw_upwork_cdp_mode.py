from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    sb.activate_cdp_mode()
    sb.goto("https://www.upwork.com/nx/search/jobs/")
    sb.sleep(2)
    sb.solve_captcha()
    sb.sleep(1)
    sb.click('input[type="search"]')
    sb.sleep(1)
    sb.press_keys('input[type="search"]', "WordPress\n")
    sb.sleep(2)
    print(sb.get_text('[data-test="JobsList"]'))
    sb.save_screenshot_to_logs()
