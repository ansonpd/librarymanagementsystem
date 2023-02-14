from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ]
        
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'
def get_expiry():
    return datetime.today() + timedelta(days=15)


class IssuedBook(models.Model):
    enrollment=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment

 

class Books():
    def __init__(self):
       return
    def another_method(self):
       return


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Product")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/products/' )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price" )
    stock = models.PositiveIntegerField(verbose_name="Stock")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug'] 
        ]
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name


class Order(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=16)
	address = models.CharField(max_length=150)
	district = models.CharField(max_length=30)
	payment_method = models.CharField(max_length = 20)
	transaction_id = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return 'Order {}'.format(self.id)


 
