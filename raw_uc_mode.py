from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    sb.goto("https://seleniumbase.io/hobbit/login")
    sb.click("button span#mySpan")
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    sb.goto("https://www.virtualmanager.com/en/login")
    print(sb.get_page_title())
    sb.solve_captcha()  # Only used if needed
    sb.assert_element('input[name*="email"]')
    print(sb.get_page_title())
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
