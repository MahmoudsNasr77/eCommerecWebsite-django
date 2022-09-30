from email.policy import default
from random import choices
from django.utils.text import slugify
from django.db import models
class saller(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    profile=models.TextField(blank=True,max_length=200)
    photo= models.ImageField(upload_to='saller/images',default='image.png')
   
    def __str__(self) :
        return self.name
CATEGORY_TYPE=(('Clothes','Clothes'),
             ('Technology','Technology'),
            ('Furniture','Furniture'),
            ('No Category','No Category'),
             )
class category(models.Model):
    type=models.CharField(max_length=25,choices=CATEGORY_TYPE)
    def __str__(self):
        return self.type
class product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=2000,blank=True)
    price=models.IntegerField()
    saller=models.ForeignKey(saller,related_name="Product_Saller",on_delete=models.DO_NOTHING)
    photo= models.ImageField(upload_to='product/images',default='image.png')
    category_type=models.ForeignKey(category,on_delete=models.CASCADE)
    is_publish=models.BooleanField(default=True)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self) :
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(product,self).save(*args,**kwargs)

    
