from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="products"
urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('products',views.products,name="productslist"),
    path('products/techon',views.techon,name="techon"),
    path('products/furniture',views.furniture,name="furniture"),
    path('products/clothes',views.clothes,name="clothes"),
    path('products/<str:slug>/Buy',views.Buy,name="BuyProudct"),
    path('products/Buy/done',views.done,name="done"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
