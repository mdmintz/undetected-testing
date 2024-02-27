from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    sb.driver.uc_open_with_reconnect("https://nopecha.com/demo/turnstile", 4.5)
    sb.driver.uc_switch_to_frame("#example-container5 iframe")
    sb.driver.uc_click("span.mark")

    # Only verification steps after this line

    sb.switch_to_frame("#example-container0 iframe")
    sb.assert_element("circle.success-circle")
    sb.switch_to_parent_frame()
    sb.switch_to_frame("#example-container5 iframe")
    sb.assert_element("svg#success-icon", timeout=3)
    sb.switch_to_parent_frame()
    sb.set_messenger_theme(location="top_center")
    sb.post_message("Selenium wasn't detected!", duration=3)
