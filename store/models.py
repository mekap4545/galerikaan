from django.db import models
from category.models import Category
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import intcomma
from djmoney.models.fields import MoneyField
from ckeditor.fields import RichTextField
# Create your models here.

class Product(models.Model):
    başlık    = models.CharField(max_length=200, unique=True)
    tarih =  models.CharField(max_length=200)
    marka =  models.CharField(max_length=200)
    seri =  models.CharField(max_length=200)
    model =  models.CharField(max_length=200)
    yıl =  models.CharField(max_length=200)
    yakıt =  models.CharField(max_length=200)
    vites =  models.CharField(max_length=200)
    km =  models.CharField(max_length=200)
    kasatipi =  models.CharField(max_length=200)
    motorgucu  = models.CharField(max_length=200)
    motorhacmi = models.CharField(max_length=200)
    çekiş =  models.CharField(max_length=200)
    renk =  models.CharField(max_length=200)
    garanti =  models.CharField(max_length=200)
    plaka =  models.CharField(max_length=200)
    kimden =  models.CharField(max_length=200)
    takas =  models.CharField(max_length=200)
    durumu =  models.CharField(max_length=200)
    boya =  models.CharField(max_length=200)
    degisen =  models.CharField(max_length=200)
    guvenlik =  models.CharField(max_length=200)
    icdonanim =  models.CharField(max_length=200)
    dişdonanım =  models.CharField(max_length=200)
    multimedya =  models.CharField(max_length=200)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = RichTextField(blank=True)
    fiyat           = MoneyField(max_digits=14, decimal_places=2, default_currency='Turkish Lira')
    #fiyat           = models.DecimalField(max_digits=14, decimal_places=2)
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.başlık

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.başlık

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'