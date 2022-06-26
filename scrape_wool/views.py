from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .utils import addItem, getItem
from .models import WoolItem
import pandas as pd
from django.forms.models import model_to_dict
from django.template import loader
# Create your views here.
def index(request):
    WoolItem.objects.all().delete()
    required_products_path = "data/required_products.json"
    required_products = pd.read_json(required_products_path).to_dict('records')
    for wool_item in required_products:
        addItem(wool_item)
    wool_items = getItem()
    template = loader.get_template('scrape_wool/index.html')
    context = {
        'available_wool_list':wool_items
    }
    return HttpResponse(template.render(context,request))



