from seleniumbase import SB

with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://seleniumbase.io/other/drag_and_drop"
    sb.activate_cdp_mode(url)
    sb.assert_element_not_visible("#div1 img#drag1")
    sb.cdp.gui_drag_and_drop("#drag1", "#div1")
    sb.assert_element("#div1 img#drag1")
    sb.sleep(1)
