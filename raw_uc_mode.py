"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB


def get_element_screen_position(driver, selector):
    element = driver.find_element(selector)
    element_location = element.location
    window_position = driver.get_window_position()
    window_size = driver.get_window_size()
    window_bottom_y = window_position["y"] + window_size["height"]
    viewport_height = driver.execute_script("return window.innerHeight;")
    # viewport_width = driver.execute_script("return window.innerWidth;")
    viewport_x = window_position["x"] + element_location["x"]
    viewport_y = window_bottom_y - viewport_height
    element_pos_x = element_location["x"]
    element_pos_y = element_location["y"]
    return (viewport_x + element_pos_x, viewport_y + element_pos_y)


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
    sb.switch_to_frame("iframe")
    x, y = get_element_screen_position(sb.driver, "span")
    sb.disconnect()
    sb.sleep(1)
    import pyautogui
    pyautogui = get_configured_pyautogui(pyautogui)
    pyautogui.click(x=x + 14, y=y + 14)
    sb.sleep(4)
    sb.connect()
    # print(sb.get_page_title())
    # sb.uc_gui_handle_cf()  # Ready if needed!
    print(sb.get_page_title())
    sb.assert_element('input[name*="email"]')
    sb.assert_element('input[name*="login"]')
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
