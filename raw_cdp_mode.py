"""CDP Mode for evading bot-detection."""
from seleniumbase import sb_cdp

try:
    sb = sb_cdp.Chrome()
    sb.goto("https://browserscan.net/bot-detection")
    sb.assert_element('strong:contains("Normal")')
    sb.sleep(1)
    sb.goto("https://bot.sannysoft.com/")
    sb.assert_element(".passed")
    sb.assert_element_not_visible(".failed")
    sb.sleep(1)
    sb.goto("https://www.planetminecraft.com/account")
    sb.type('[name="email"]', "Name123")
    sb.type('[name="password"]', "Pass")
    sb.solve_captcha()
    sb.assert_element('input[name="login"]')
    sb.assert_element_not_visible("input[disabled]")
    sb.save_screenshot_to_logs()
    print("All stealth tests passed successfully!")
    sb.sleep(1)
    sb.quit()
except Exception as e:
    print(e)
