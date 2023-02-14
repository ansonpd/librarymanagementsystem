from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView   
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view),


    path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),
    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),
         

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent),
         

    path('purchase/', views.product, name='purchase'),
    path('order/<int:product_id>/',views.purchase_view,name='order'),
    path('about',views.about_view),
    path('details/',views.order_view,name='details'),
    path('sucessful',views.sucessful_view,name='sucessful'),
                    
      
 
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)