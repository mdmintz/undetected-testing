"""UC Mode has PyAutoGUI methods for CAPTCHA-bypass."""
from seleniumbase import SB

with SB(test=True) as sb:
    url = "https://my-user-agent.com/"
    sb.open(url)
    sb.highlight("#ua_string")
    user_agent_detected = sb.get_text("#ua_string")
    print("\n\nUser-Agent: %s\n\n" % user_agent_detected)
