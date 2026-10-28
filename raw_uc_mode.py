from seleniumbase import SB

with SB(uc=True, test=True, incognito=True) as sb:
    sb.goto("https://seleniumbase.io/hobbit/login")
    sb.sleep(1)
    sb.click("button span#mySpan")
    sb.sleep(1.5)
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True, incognito=True) as sb:
    sb.goto("https://www.virtualmanager.com/en/login")
    sb.sleep(1.5)
    print(sb.get_page_title())
    sb.solve_captcha()  # Only used if needed
    sb.sleep(2)
    sb.assert_element('input[name*="email"]')
    print(sb.get_page_title())
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
