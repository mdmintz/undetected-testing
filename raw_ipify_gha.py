import os
from seleniumbase import SB

# Regular Mode (no proxy)
with SB() as sb:
    sb.open("https://api.ipify.org")
    print("Full IP from ipify:")
    print(sb.get_page_source())

try:
    proxy = os.environ["proxy_1"]
except Exception:
    proxy = None

if proxy:
    print("First part of proxy IP:")
    print(proxy.split("@")[-1].split(":")[0].split(".")[0])

# Regular Mode with proxy
with SB(proxy=proxy) as sb:
    sb.open("https://api.ipify.org")
    print("Full IP from ipify:")
    print(sb.get_page_source())

# CDP Mode
with SB(proxy=proxy, uc=True) as sb:
    sb.activate_cdp_mode("https://api.ipify.org")
    print("Full IP from ipify:")
    print(sb.get_page_source())
