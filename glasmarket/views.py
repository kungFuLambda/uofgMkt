from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #contruct dictionary to pass values to the {{boldmessage}} variable
    context_dict = {}
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'index'
    context_dict['navBar'] = ['index','marketplace','about','profile']




    return render(request,'glasmarket/index.html',context_dict)