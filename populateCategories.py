import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasmarketProject.settings') 
from PIL import Image
import django 
django.setup()
from glasmarket.models import Category,Listing,User
def populate():

    users = []
    product = [] 
    cats = ['tech','hobby','stationary','clothes']


    for i in range(20):
        name = "user"+str(i)
        dicti = {}
        dicti["name"] = name
        dicti["email"] = name+"@gmail.com"
        dicti["fullName"] = name + " surname"
        dicti["phone"] = 123456780+i
        dicti['listing'] = product
        dicti['password'] = name + "psw"
        users.append(dicti)

    for cat in cats:
        add_category(cat)

    
        
    
def add_category(catName):
    c = Category.objects.get_or_create(name=catName)[0]
    c.save()
    return c

def add_user(name,email,fullName,phone,password):
    u = User.objects.get_or_create(username=name,email=email,fullName=fullName,phone=phone,password=password)[0]
    u.save()
    return u





if __name__=='__main__':
    populate()