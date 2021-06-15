from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("./chromedriver")
browser.get(START_URL)
time.sleep(10)


headers = ["Name", "Distance", "Mass", "Radius"]
star_data = []


def scrape():
    for i in range(0, 97):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            # print(td_tags[1].text)
            for index, td_tag in enumerate(td_tags):
                if index == 1 or index == 3 or index ==5 or index == 6:
                    try:
                        temp_list.append(td_tag.text)
                    except:
                        temp_list.append('')
            star_data.append(temp_list)
    with open("scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
    

scrape()
browser.close()
