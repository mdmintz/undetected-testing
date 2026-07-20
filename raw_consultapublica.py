from seleniumbase import sb_cdp

sb = sb_cdp.Chrome(incognito=True)
url = "https://consultapublica.tjpb.jus.br/pje/ConsultaPublica/listView.seam"
sb.goto(url)
sb.sleep(3)
sb.solve_captcha()
sb.sleep(3)
sb.save_screenshot_to_logs()
