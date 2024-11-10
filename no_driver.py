import nodriver
import time
from sbvirtualdisplay import Display
from seleniumbase.fixtures import shared_utils


async def main():
    display = Display(visible=False, size=(1366, 768))
    display.start()
    browser = await nodriver.start()
    page = await browser.get("https://www.virtualmanager.com/en/login")
    time.sleep(3)
    print(await page.evaluate("document.title"))
    display.stop()

if __name__ == "__main__":
    shared_utils.pip_install("websockets", version="13.1")
    nodriver.loop().run_until_complete(main())
