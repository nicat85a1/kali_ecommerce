from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
# Create your views here.
from product.forms import ProductForm
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    return render(request, 'web/home.html')

@login_required(login_url="login_view")
def create_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("home")
    return render(request, "product/create_product.html", {'form':form})

@login_required(login_url="login_view")
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    #product = Product.objects.filter(id=id).first()
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "product/update_product.html", {'form':form})

def detail_product(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request, "product/detail_product.html", {'product':product})

@login_required(login_url="login_view")
def delete_product(request,id):
    product = Product.objects.filter(id=id, user=request.user).first()
    if product is None:
        return HttpResponse(f"get o terefde oyna ay {request.user}")
    #product = get_object_or_404(Product,id=id, user=request.user)
    product.delete()
    return redirect("home")