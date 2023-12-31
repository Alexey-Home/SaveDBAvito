# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import re

import additional as ad


def get_links(page_with_links):
    result = {}
    print("Открываю сохраненую страницу...")
    path = "pages/" + page_with_links
    with open(path, "r", encoding="utf-8") as file:
        page_html = file.read()

    soup = BeautifulSoup(page_html, "lxml")
    first_class_name = re.compile(r"^popular-rubricator-links-[A-Za-z0-9]*$")
    second_class_name = re.compile(r"^popular-rubricator-row-[A-Za-z0-9]*$")
    links = soup.find("div", class_=first_class_name).find_all("div", class_=second_class_name)
    if links:
        for link in links:
            result[link.get_text(separator="|").split("|")[0].lower()] = \
                "https://www.avito.ru" + link.find("a").get("href")
    else:
        return None

    return result


def get_links_cars(name_page, page_link):

    def get_links(result, number_page, count):
        print("Открываю сохраненую страницу...")
        with open("pages/" + name_page, "r", encoding="utf-8") as file:
            page_html = file.read()
        soup = BeautifulSoup(page_html, "lxml")
        if count == 1:
            print("Определяю количество страниц...")
            # собираем количество страниц
            req_number_page = re.compile(
                "styles-module-item-[a-zA-Z0-9]+ styles-module-item_size_s-[a-zA-Z0-9]+ styles-module-item_last-[a-zA-Z0-9]+ styles-module-item_link-_[a-zA-Z0-9]+")
            number_page = soup.find("a", class_=req_number_page).text

        re_car = re.compile("iva-item-root-[a-zA-Z0-9_]* photo-slider-slider-[a-zA-Z0-9_]* iva-item-list-[a-zA-Z0-9_]* iva-item-redesign-[a-zA-Z0-9_]* iva-item-responsive-[a-zA-Z0-9_]* items-item-[a-zA-Z0-9_]* items-listItem-[a-zA-Z0-9_]* js-catalog-item-enum")
        re_car_url = re.compile("iva-item-sliderLink-[a-zA-Z0-9_]")
        cars_links = soup.find_all("div", class_=re_car)
        print("Собираю ссылки машин со страницы...")
        for car_link in cars_links:
            result[car_link.get("id")] = "https://www.avito.ru" + car_link.find("a", class_=re_car_url).get("href")
        return result, number_page

    result = {}

    number_page = 2
    count = 1

    # открываем страницы по номерам и сохраняем в файл
    while count != int(number_page):
        link = page_link + "&p=" + str(count)
        ad.get_page(link, name_page)
        result, number_page = get_links(result, number_page, count)
        print(len(result))
        count += 1
    return result




