import fasteners
import math
import os
import sys
from seleniumbase import SB
from seleniumbase import config as sb_config
from seleniumbase.fixtures import constants
from seleniumbase.fixtures import shared_utils


def get_configured_pyautogui(pyautogui_copy):
    if (
        shared_utils.is_linux()
        and hasattr(pyautogui_copy, "_pyautogui_x11")
        and "DISPLAY" in os.environ.keys()
    ):
        if (
            hasattr(sb_config, "_pyautogui_x11_display")
            and sb_config._pyautogui_x11_display
            and hasattr(pyautogui_copy._pyautogui_x11, "_display")
            and (
                sb_config._pyautogui_x11_display
                == pyautogui_copy._pyautogui_x11._display
            )
        ):
            pass
        else:
            import Xlib.display
            pyautogui_copy._pyautogui_x11._display = (
                Xlib.display.Display(os.environ['DISPLAY'])
            )
            sb_config._pyautogui_x11_display = (
                pyautogui_copy._pyautogui_x11._display
            )
    return pyautogui_copy


def get_gui_element_rect(sb, selector, by="css selector"):
    element = sb.wait_for_element_present(selector, by=by, timeout=1)
    element_rect = element.rect
    e_width = element_rect["width"]
    e_height = element_rect["height"]
    i_x = 0
    i_y = 0
    window_rect = sb.get_window_rect()
    w_bottom_y = window_rect["y"] + window_rect["height"]
    viewport_height = sb.execute_script("return window.innerHeight;")
    x = math.ceil(window_rect["x"] + i_x + element_rect["x"])
    y = math.ceil(w_bottom_y - viewport_height + i_y + element_rect["y"])
    y_scroll_offset = sb.execute_script("return window.pageYOffset;")
    y = int(y - y_scroll_offset)
    return ({"height": e_height, "width": e_width, "x": x, "y": y})


def get_gui_element_center(sb, selector, by="css selector"):
    element_rect = get_gui_element_rect(sb, selector, by=by)
    x = element_rect["x"] + (element_rect["width"] / 2.0) + 0.5
    y = element_rect["y"] + (element_rect["height"] / 2.0) + 0.5
    return (x, y)


def __gui_drag_drop(sb, x1, y1, x2, y2, timeframe=0.25, uc_lock=False):
    import pyautogui
    pyautogui = get_configured_pyautogui(pyautogui)
    screen_width, screen_height = pyautogui.size()
    if x1 < 0 or y1 < 0 or x1 > screen_width or y1 > screen_height:
        raise Exception(
            "PyAutoGUI cannot drag-drop from point (%s, %s)"
            " outside screen. (Width: %s, Height: %s)"
            % (x1, y1, screen_width, screen_height)
        )
    if x2 < 0 or y2 < 0 or x2 > screen_width or y2 > screen_height:
        raise Exception(
            "PyAutoGUI cannot drag-drop to point (%s, %s)"
            " outside screen. (Width: %s, Height: %s)"
            % (x2, y2, screen_width, screen_height)
        )
    if uc_lock:
        gui_lock = fasteners.InterProcessLock(
            constants.MultiBrowser.PYAUTOGUILOCK
        )
        with gui_lock:  # Prevent issues with multiple processes
            pyautogui.moveTo(x1, y1, 0.25, pyautogui.easeOutQuad)
            sb.sleep(0.05)
            if "--debug" in sys.argv:
                print(" <DEBUG> pyautogui.moveTo(%s, %s)" % (x1, y1))
            pyautogui.dragTo(x2, y2, button="left", duration=timeframe)
    else:
        # Called from a method where the gui_lock is already active
        pyautogui.moveTo(x1, y1, 0.25, pyautogui.easeOutQuad)
        sb.sleep(0.05)
        if "--debug" in sys.argv:
            print(" <DEBUG> pyautogui.dragTo(%s, %s)" % (x2, y2))
        pyautogui.dragTo(x2, y2, button="left", duration=timeframe)


def gui_drag_drop_points(sb, x1, y1, x2, y2, timeframe=0.35):
    gui_lock = fasteners.InterProcessLock(
        constants.MultiBrowser.PYAUTOGUILOCK
    )
    with gui_lock:  # Prevent issues with multiple processes
        import pyautogui
        pyautogui = get_configured_pyautogui(pyautogui)
        width_ratio = 1.0
        if shared_utils.is_windows():
            window_rect = sb.get_window_rect()
            width = window_rect["width"]
            height = window_rect["height"]
            win_x = window_rect["x"]
            win_y = window_rect["y"]
            scr_width = pyautogui.size().width
            sb.maximize()
            sb.sleep(0.05)
            win_width = sb.get_window_size()["width"]
            width_ratio = round(float(scr_width) / float(win_width), 2)
            width_ratio += 0.01
            if width_ratio < 0.45 or width_ratio > 2.55:
                width_ratio = 1.01
            sb_config._saved_width_ratio = width_ratio
            sb.minimize()
            sb.sleep(0.5)
            sb.set_window_rect(win_x, win_y, width, height)
            sb.sleep(0.5)
            x1 = x1 * width_ratio
            y1 = y1 * width_ratio
            x2 = x2 * width_ratio
            y2 = y2 * width_ratio
        sb.bring_active_window_to_front()
        __gui_drag_drop(
            sb, x1, y1, x2, y2, timeframe=timeframe, uc_lock=False
        )
    sb.sleep(0.05)


def gui_drag_and_drop(sb, drag_selector, drop_selector, timeframe=0.35):
    sb.bring_active_window_to_front()
    x1, y1 = get_gui_element_center(sb, drag_selector)
    sb.sleep(0.05)
    x2, y2 = get_gui_element_center(sb, drop_selector)
    sb.sleep(0.05)
    gui_drag_drop_points(sb, x1, y1, x2, y2, timeframe=timeframe)


# UC Mode
with SB(
    uc=True, test=True, incognito=True, xvfb_metrics="1920,1080"
) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.uc_open_with_reconnect(url)
    sb.assert_element_not_visible("#div1 img#drag1")
    gui_drag_and_drop(sb, "#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)


# CDP Mode
with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode(url)
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.cdp.gui_drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)


# CDP Mode reconnected
with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode(url)
    sb.reconnect()
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.cdp.gui_drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)

# CDP Mode reconnected with clean tab and custom code
with SB(
    uc=True, test=True, incognito=True, xvfb_metrics="1920,1080"
) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode()
    sb.cdp.open_new_tab(url)
    sb.cdp.switch_to_tab(0)
    sb.cdp.close_active_tab()
    sb.cdp.switch_to_newest_tab()
    sb.reconnect()
    sb.assert_element_not_visible("#div1 img#drag1")
    gui_drag_and_drop(sb, "#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)
