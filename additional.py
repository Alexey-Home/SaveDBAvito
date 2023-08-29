# -*- coding: utf8 -*-
import random
import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_page(url, name_page):
    """Открывает страницу в Chrome-браузере и сохраняет ее в файл"""
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")

    # accept
    options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                         "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")

    # for ChromeDriver version 79.0.3945.16 or over
    options.add_argument("--disable-blink-features=AutomationControlled")

    #headless mode
    # options.add_argument("--no-sandbox")
    # options.headless = True

    if platform == "win32":
        path = r"chromedriver.exe"
    else:
        path = "/home/my_bot/chromedriver"
    s = Service(path)
    driver = webdriver.Chrome(service=s, options=options)

    try:
        print("Открываю страницу...")
        driver.get(url=url)
        time.sleep(10)
        time.sleep(random.randint(0, 5))

        print("Сохраняю страницу...")
        path = "pages\\" + name_page
        with open(path, "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        print("Готово!")

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()
