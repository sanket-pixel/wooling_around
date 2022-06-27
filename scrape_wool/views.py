from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .utils import addItem, getItem
from .models import WoolItem
import pandas as pd
from django.forms.models import model_to_dict
from django.template import loader
import json
# Create your views here.
def index(request):
    # delete all old data from db
    WoolItem.objects.all().delete()
    # get products and brand for which wool info is needed
    required_products_path = "data/required_products.json"
    required_products = pd.read_json(required_products_path).to_dict('records')
    # fetch data for all items and store in db
    for wool_item in required_products:
        addItem(wool_item)
    # get all stored items
    wool_items = getItem()
    # send the data to the template
    template = loader.get_template('scrape_wool/index.html')
    context = {
        'available_wool_list':wool_items
    }
    # store the data in local json file
    save_product_path = "data/saved_products.json"
    wool_json_list = []
    for wool in wool_items:
        w = model_to_dict(wool)
        wool_json_list.append(w)
    with open(save_product_path, 'w') as fp:
        json.dump(wool_json_list, fp)
    return HttpResponse(template.render(context,request))



