from bs4 import BeautifulSoup
import time
import csv

start_url = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\DOCTOR PC\Documents\pythonprojects\chromedriver_win32\chromedriver")

def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    stars_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "List of brightest stars and other record stars"}):
            tr_tag = ul_tag.find_all("tr")
            temp_list = []
            for index, tr_tag in enumerate(tr_tag):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            stars_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)''
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)

scrape()