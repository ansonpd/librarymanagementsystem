from django.contrib import admin
from .models import Book,StudentExtra,IssuedBook,Category,Product,Order
###

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)

class Categoryadmin(admin.ModelAdmin):
    pass
admin.site.register(Category, Categoryadmin)

class Productadmin (admin.ModelAdmin):
    pass
admin.site.register(Product, Productadmin )
 
class Orderadmin(admin.ModelAdmin):
	 pass
admin.site.register(Order, Orderadmin)