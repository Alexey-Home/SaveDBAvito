# -*- coding: utf8 -*-
import json
import additional as ad
import avitoparsing as avp
import cars
import time


def main():
    # st = time.time()
    # links = collect_links()
    # print(links)
    #
    # with open('data/links.txt', 'w', encoding="utf-8") as outfile:
    #     json.dump(links, outfile, ensure_ascii=False)
    # et = time.time()

    # print(et-st)

    with open('data/links.txt', encoding="utf-8") as json_file:
        data = json.load(json_file)


    for company, models in data.items():
        for model, link in models.items():
            name_page = model + ".html"
            ad.get_page(link, name_page)
            cars_links = avp.get_links_cars(name_page, link)
            data[company][model] = cars_links
            pass



def collect_links():
    url = "https://www.avito.ru/all/avtomobili/"
    links = {}
    name_page = "all_auto.html"
    ad.get_page(url, name_page)
    links_company = avp.get_links(name_page)
    name_page = "model.html"
    for name, link in links_company.items():
        ad.get_page(link, name_page)
        links[name] = avp.get_links(name_page)
        print(links)
    return links




if __name__ == "__main__":
   main()