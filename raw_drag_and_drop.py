from seleniumbase import SB

# UC Mode
with SB(
    uc=True, test=True, incognito=True, xvfb_metrics="1920,1080"
) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.uc_open_with_reconnect(url)
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)

# CDP Mode
with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode(url)
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)


# CDP Mode reconnected
with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode(url)
    sb.reconnect()
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)

# CDP Mode reconnected with clean tab and custom code
with SB(
    uc=True, test=True, incognito=True, xvfb_metrics="1920,1080"
) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode()
    sb.open_new_tab(url)
    sb.switch_to_tab(0)
    sb.close_active_tab()
    sb.switch_to_newest_tab()
    sb.reconnect()
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)
