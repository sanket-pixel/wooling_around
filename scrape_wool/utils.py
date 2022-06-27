from bs4 import BeautifulSoup
from .models import WoolItem
import requests

def addItem(data):
    data, matched_flag = scrape_informatino(data["brand"], data["product"])
    if matched_flag :
        w = WoolItem(**data)
        w.save()
        return w,True
    else:
        return None, False

def getItem():
    items = WoolItem.objects.all()
    return items

def get_sub_url(brand_name,product_name):
    brand_name = brand_name.lower()
    product_name = " ".join(product_name.split())
    product_name = product_name.replace(" ","-").lower()
    combined_brand_product_name = f'{brand_name}-{product_name}'
    return f'{brand_name}/{combined_brand_product_name}'


def scrape_informatino(brand_name = "DMC", product_name = "Natura Medium"):
    # define the target url by converting brand and product to small case.
    # then combine them as per the pattern of the website.
    base_url = "https://www.wollplatz.de/wolle"
    sub_url = get_sub_url(brand_name, product_name)
    target_url = f'{base_url}/{sub_url}'
    # make request to the target url
    re = requests.get(target_url)
    # if url returns 200, it means the product exists.
    if re.status_code!=200:
        matched_flag = False
        return {}, matched_flag
    else:
        matched_flag = True
    # parse the html page using BeautifulSoup
    soup = BeautifulSoup(re.text, "html.parser")
    # get the div containing the table using id
    # this info is found using inspect element of the browser.
    table_data = list(soup.find("div", {"id": "pdetailTableSpecs"}).children)[3]
    specs = dict([[cell.text for cell in row("td")]
             for row in table_data("tr")])
    # get price, currency, needle size and composition
    price = soup.find("span", {"class": "product-price-amount"}).text
    price = float(price.replace(",", "."))
    currency = soup.find("span", {"class": "product-price-currency"}).text.strip()
    data = {
        "brand":brand_name,
        "product":product_name,
        "price" : price,
        "currency" : currency,
        "needle_size": specs["Nadelstärke"],
        "composition": specs["Zusammenstellung"],
        "link": target_url
    }
    return data, matched_flag