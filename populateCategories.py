import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasmarketProject.settings') 
from PIL import Image
import django 
django.setup()
from glasmarket.models import Category,Listing,User
def populate():

    users = []
    product = [] 
    cats = ['tech','hobby','stationary','clothes','books','flatmates','services',]

    for cat in cats:
        add_category(cat)
        print(cat + " added")

    
        
    
def add_category(catName):
    c = Category.objects.get_or_create(name=catName)[0]
    c.save()
    return c



if __name__=='__main__':
    populate()