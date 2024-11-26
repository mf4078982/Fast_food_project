from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import Order
from .forms import OrderForm


# Create your views here.
def order(request):
    return render(request, 'men.html')

# views.py

def order_view(request):
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after order
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})
    




def order_submit(request):
    if request.method == "POST":
        # Handle form submission logic here
        return HttpResponse("Order submitted successfully!")
    
        
    return HttpResponse("Invalid request method.")
    


def order_now(request, food_name):
    food_image_url = f"/static/images/{food_name.lower().replace(' ', '_')}.jpg"  # Adjust path as needed
    success = False

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        else:
            success = False
    else:
        form = OrderForm()

    return render(request, "order_now.html", {
        "form": form,
        "food_name": food_name,
        "food_image_url": food_image_url,
        "success": success,
    })



def burgar(request, burgar_name):
    return render(request,'burgar.html')
    
    
    
    
def pizza(request, pizza_name):
    return render(request,'pizza.html')

def pasta(request,pasta_name):
    return render(request,'pasta.html')

def fries(request,fries_name):
    return render(request,'fries.html')

def samosa(request,samosa_name):
    return render(request,'samosa.html')

def content(request):
    return render(request, 'content.html')



def chicken_view(request, food_item):
    return render(request, 'chicken.html')
