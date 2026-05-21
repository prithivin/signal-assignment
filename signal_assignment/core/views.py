import threading
import time

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from .models import TestModel
from core.rectangle import Rectangle

# Create your views here.
def display_home_page(request):
    return render(request, 'core/home.html')

# Question 1 and 2
def test_signal_behavior(request):
    start = time.time()
    
    print("Caller Thread ID: ", threading.get_ident())
    
    TestModel.objects.create(name="Signal Test")
    
    end = time.time()
    
    return HttpResponse(f"Request completed in {end - start:.2f} seconds")

# Question 3
def test_transaction_behavior(request):
    try:
        with transaction.atomic():
            
            TestModel.objects.create(name="Transaction Test")
            
            print("Object created")
            
            raise Exception("Force rollback")
        
    except Exception as e:
        print("Transaction rolled back")
        
        count = TestModel.objects.filter(name="Transaction Test").count()
        
        return HttpResponse(f"Objects in DB after rollback: {count}")

# Question on custom classes    
def test_rectangle_iterator(request):
    rect = Rectangle(10, 5)
    
    context_list =[]
    for item in rect:
        context_list.append(item)
        
    context = {'items': context_list}    
    return render(request, 'core/rectangle.html', context)
    
    

