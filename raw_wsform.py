from seleniumbase import sb_cdp

sb = sb_cdp.Chrome(locale="en", incognito=True)
sb.goto("https://wsform.com/demo/")
sb.sleep(3)
sb.solve_captcha()
sb.sleep(3)
sb.save_screenshot_to_logs()
