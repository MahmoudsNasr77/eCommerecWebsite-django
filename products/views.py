from multiprocessing import context
from django.shortcuts import redirect, render
from .models import product,category,saller
from django.core.paginator import Paginator
from .forms import BuyingForm
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter
def home(request):
    products=product.objects.order_by('name').reverse()[:3]
    sallers=saller.objects.all()
    return render(request,'products/home.html',{"products":products,'sallers':sallers})

def products(request):
    products=product.objects.all()
    myfilter=ProductFilter(request.GET,queryset=products)
    products=myfilter.qs
    categor=category.objects.all()
    paginator=Paginator(products,6)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    context={'products':paged_product,'myfilter':myfilter,'categor':categor}
    return render(request,'products/proudct_list.html',context)
def techon(request):
    products=product.objects.filter(category_type=2)
    myfilter=ProductFilter(request.GET,queryset=products)
    products=myfilter.qs
    paginator=Paginator(products,6)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    context={'products':paged_product,'myfilter':myfilter}
    return render(request,'products/techonloge.html',context)
def furniture(request):
    products=product.objects.filter(category_type=3)
    myfilter=ProductFilter(request.GET,queryset=products)
    products=myfilter.qs
    paginator=Paginator(products,6)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    context={'products':paged_product,'myfilter':myfilter}
    return render(request,'products/furniture.html',context)
def clothes(request):
    products=product.objects.filter(category_type=1)
    myfilter=ProductFilter(request.GET,queryset=products)
    products=myfilter.qs
    paginator=Paginator(products,6)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    context={'products':paged_product,'myfilter':myfilter}
    return render(request,'products/clothes.html',context)
def done(request):
    return render(request,"products/buyingdone.html")
@login_required
def Buy(request,slug):
    Singel_product=product.objects.get(slug=slug)
    if request.method == 'POST':
        form =BuyingForm(request.POST)
        if form.is_valid():
            return redirect('products:done')
            
    else:
        form =BuyingForm(request.POST)
    return render(request, 'products/buyingform.html', {'Singel_product':Singel_product,'form': form})
def about(request):
    return render(request,"products/about.html")
    