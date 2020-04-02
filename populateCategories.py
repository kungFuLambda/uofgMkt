import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasmarketProject.settings') 
import random
import django 
django.setup()
from glasmarket.models import Category,Listing,User,UserProfile
def populate():

    passw= "testing12399"
    users = []
    product = [] 
    cats = ['tech','hobby','stationary','clothes','books','flatmates','services',]
    description = "This is a user listing, with price, link to seller and name, and picture, you can click on the picture to make it big"
    product_names = []





    add_user("len","leones.tadina@gmail.com","")
    with open("objectNames.txt") as namez:
        for line in namez:
            product_names.append(line.strip())


    for cat in cats:
        add_category(cat)
        print(cat + " added")

    with open("listOfNames.txt") as names:
        for line in names:
            usr = add_user(line.strip(),line.strip()+"@gmail.com",passw)
            print(line.strip() +" added")
            ls = add_listing(Category.objects.get(name=cats[random.randint(1,5)]),product_names[random.randint(1,len(product_names)-1)],usr,description)
            
    for p in product_names:
        ls = add_listing(Category.objects.get(name=cats[random.randint(1,5)]),p,UserProfile.objects.get(user=User.objects.get(username="len")),description)
        
    
def add_category(catName):
    c = Category.objects.get_or_create(name=catName)[0]
    c.save()
    return c

def add_user(username,email,password):
    u = User.objects.get_or_create(username=username,email=email,password=password)[0]
    p = UserProfile.objects.get_or_create(user=u)[0]
    p.save()
    return p
    
def add_listing(category,name,seller,description):
    p = Listing.objects.get_or_create(name=name,price=random.randint(1,101),seller=seller,category=category,description=description)[0]
    p.save()
    return p

if __name__=='__main__':
    populate()