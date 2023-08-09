from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
        soup = BeautifulSoup(browser.page_source, "html.parser")
        start_table = soup.find_all("table",atts={"class","wikitable sortable jquery-tablesorter"})
        table_body = soup.find_all("tbody")
        table_rows = soup.find_all("tr")

        for row in table_rows:
            table_cols = row.find_all("td")
            # print(table_cols)
            temp_list = []
            for col_data in table_cols:
                # print(col_data.text)
                data = col_data.text.strip()
                temp_list.append(data)

        scraped_data.append(temp_list)
# Calling Method
scrape()

# Define Header
headers = ["Star_name", "Distance", "Radius", "Mass", "Luminosity"]

# Define pandas DataFrame 
stars_df_1 = pd.DataFrame(scraped_data, columns=headers)

# Convert to CSV
stars_df_1.to_csv('updated_scraped_data.csv',index=True, index_label="id")