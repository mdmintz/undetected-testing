# undetected-testing

Find out if SeleniumBase can fool sites with anti-bot services

First:

```bash
> pip install -U seleniumbase
```

Then:

```bash
> pytest test_verify_undetected.py --uc --incognito -s -q

 Success! Website did not detect Selenium!
.
-------- Latest Logs dir: /HOME/undetected-testing/latest_logs/ ---------
1 passed in 6.70s
```

```bash
> python verify_undetected.py

 Success! Website did not detect Selenium!

Screenshot saved to: now_secure_image.png
```
