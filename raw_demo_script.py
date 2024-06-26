"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://my-user-agent.com/"
    sb.uc_open(url)
    sb.highlight("#ua_string")
    user_agent_detected = sb.get_text("#ua_string")
    print("\n\nUser-Agent: %s\n\n" % user_agent_detected)

with SB(uc=True, incognito=True, test=True) as sb:
    sb.driver.uc_open_with_reconnect("https://pixelscan.net/", 10)
    sb.remove_elements("jdiv")  # Remove chat widgets
    print(sb.get_text())
