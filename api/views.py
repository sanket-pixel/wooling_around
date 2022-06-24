from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import WoolItem
from .serializers import ItemSerializer
from bs4 import BeautifulSoup
import requests

@api_view(['GET'])
def getData(request):
    items = WoolItem.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    data, matched_flag = scrape_informatino(request.data["brand_name"], request.data["product_name"])
    if matched_flag :
        serializer  = ItemSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':'success','content':serializer.data},status=200)
    else:
        return Response({'status': 'failed', 'content':{}}, status=404)




def get_sub_url(brand_name,product_name):
    brand_name = brand_name.lower()
    product_name = " ".join(product_name.split())
    product_name = product_name.replace(" ","-").lower()
    combined_brand_product_name = f'{brand_name}-{product_name}'
    return f'{brand_name}/{combined_brand_product_name}'

# {"brand_name": "DMC", "product_name" : "Natura"}
def scrape_informatino(brand_name = "DMC", product_name = "Natura Medium"):
    base_url = "https://www.wollplatz.de/wolle"
    sub_url = get_sub_url(brand_name, product_name)
    target_url = f'{base_url}/{sub_url}'
    re = requests.get(target_url)
    if re.status_code!=200:
        matched_flag = False
        return {}, matched_flag
    else:
        matched_flag = True
    soup = BeautifulSoup(re.text, "html.parser")
    table_data = list(soup.find("div", {"id": "pdetailTableSpecs"}).children)[3]
    specs = dict([[cell.text for cell in row("td")]
             for row in table_data("tr")])
    price = soup.find("span", {"class": "product-price-amount"}).text
    price = float(price.replace(",", "."))
    currency = soup.find("span", {"class": "product-price-currency"}).text.strip()
    data = {
        "price" : price,
        "currency" : currency,
        "needle_size": specs["Nadelstärke"],
        "composition": specs["Zusammenstellung"]
    }
    return data,matched_flag
