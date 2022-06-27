from django.test import TestCase
from .models import WoolItem
from .utils import addItem

# Create your tests here.
class WoolPriceTestCase(TestCase):
    def setUp(self):
        data1 = {"brand":"DMC", "product":"Natura XL"}
        data2 = {"brand": "Drops", "product": "Safran"}
        addItem(data1)
        addItem(data2)
    def test_product_price(self):
        wool_dmc = WoolItem.objects.get(product="Natura XL", brand="DMC")
        wool_drops = WoolItem.objects.get(product="Safran", brand="Drops")
        self.assertEqual(wool_dmc.price, 8.46)
        self.assertEqual(wool_drops.price ,1.08)


class WoolLinkTestCase(TestCase):
    def setUp(self):
        data1 = {"brand":"DMC", "product":"Natura XL"}
        data2 = {"brand": "Drops", "product": "Safran"}
        addItem(data1)
        addItem(data2)
    def test_product_price(self):
        wool_dmc = WoolItem.objects.get(product="Natura XL", brand="DMC")
        wool_drops = WoolItem.objects.get(product="Safran", brand="Drops")
        self.assertEqual(wool_dmc.link, "https://www.wollplatz.de/wolle/dmc/dmc-natura-xl")
        self.assertEqual(wool_drops.link ,"https://www.wollplatz.de/wolle/drops/drops-safran")