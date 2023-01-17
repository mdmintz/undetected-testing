# undetected-testing

Find out if [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) can fool sites that use bot-detection services.

First:

```bash
> pip install -U seleniumbase
```

Now you can try running a test ([test_verify_undetected.py](https://github.com/mdmintz/undetected-testing/blob/master/test_verify_undetected.py)) to see if SeleniumBase can fool https://nowsecure.nl/#relax, which won't let you through (normally) if an automation framework is detected:

```bash
> pytest test_verify_undetected.py --uc --incognito -s -q

 Success! Website did not detect Selenium!
.
-------- Latest Logs dir: /HOME/undetected-testing/latest_logs/ ---------
1 passed in 6.70s
```

Here's a different script for that same site, ([verify_undetected.py](https://github.com/mdmintz/undetected-testing/blob/master/verify_undetected.py)), which uses one of the other [SeleniumBase Syntax Formats](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/syntax_formats.md):

```bash
> python verify_undetected.py

 Success! Website did not detect Selenium!

Screenshot saved to: now_secure_image.png
```

--------

SeleniumBase Undetected Mode has been successful in bypassing detection on several sites that use automation-detection services:

<img width="568" alt="Undetected SeleniumBase" src="https://user-images.githubusercontent.com/6788579/213031519-0220d19f-e210-4858-b6b5-9253b112efe4.png">

In general, opening a URL to one of these sites in SeleniumBase Undetected Mode will bypass detection. However, once you start using other actions such as clicking or typing text, then they might be able to catch you IF they continue to scan your browser AFTER the initial page load. If you're only interested in opening a URL and scraping data from it, (without clicking any buttons, etc), then those sites probably won't be able to detect you.
