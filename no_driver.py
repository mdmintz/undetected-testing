import nodriver
import time
from pyvirtualdisplay.display import Display


async def main():
    browser = await nodriver.start()
    page = await browser.get("https://www.virtualmanager.com/en/login")
    time.sleep(3)
    print(await page.evaluate("document.title"))

if __name__ == "__main__":
    disp = Display(
        visible=True, size=(1366, 768), backend="xvfb", use_xauth=True
    )
    disp.start()
    nodriver.loop().run_until_complete(main())
    disp.stop()
