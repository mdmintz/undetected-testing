"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB


def get_screen_target(driver, selector):
    """Get the screen coordinates of an element's midpoint."""
    element = driver.find_element(selector)
    element_rect = element.rect
    # element_width = element_rect["width"]
    # element_height = element_rect["height"]
    window_rect = driver.get_window_rect()
    window_bottom_y = window_rect["y"] + window_rect["height"]
    viewport_height = driver.execute_script("return window.innerHeight;")
    viewport_x = window_rect["x"] + element_rect["x"]
    viewport_y = window_bottom_y - viewport_height + element_rect["y"]
    # mid_x = int(element_width / 2) + 2
    # mid_y = int(element_height / 2) + 1
    return (viewport_x, viewport_y)


def get_configured_pyautogui(pyautogui_copy):
    import os
    import Xlib.display
    pyautogui_copy._pyautogui_x11._display = (
        Xlib.display.Display(os.environ['DISPLAY'])
    )
    return pyautogui_copy


with SB(uc=True, test=True, rtf=True) as sb:
    url = "https://seleniumbase.io/hobbit/login"
    sb.uc_open_with_disconnect(url, 2)
    sb.uc_gui_press_keys("\t ")
    sb.reconnect(2)
    print(sb.get_current_url())
    sb.assert_text("Welcome to Middle Earth!", "h1")
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    url = "https://www.virtualmanager.com/en/login"
    sb.uc_open_with_reconnect(url, 6)
    x1, y1 = get_screen_target(sb.driver, "iframe")
    sb.switch_to_frame("iframe")
    span = sb.get_element("span")
    x = x1 + span.rect["x"] + int(span.rect["width"] / 2)
    y = y1 + span.rect["y"] + int(span.rect["height"] / 2)
    x, y = get_screen_target(sb.driver, "span")
    print((x, y))
    sb.disconnect()
    sb.sleep(1)
    import pyautogui
    pyautogui = get_configured_pyautogui(pyautogui)
    pyautogui.moveTo(x + 14, y + 14, 2, pyautogui.easeOutQuad)
    pyautogui.click(x + 14, y + 14)
    sb.sleep(4)
    sb.connect()
    # print(sb.get_page_title())
    # sb.uc_gui_handle_cf()  # Ready if needed!
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")

with SB(uc=True, test=True) as sb:
    url = "https://www.virtualmanager.com/en/login"
    sb.uc_open_with_disconnect(url, 6)
    pyautogui.moveTo(x + 14, y + 14, 2, pyautogui.easeOutQuad)
    pyautogui.click(x + 14, y + 14)
    sb.sleep(4)
    sb.connect()
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
