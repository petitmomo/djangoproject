from django.urls import path
from .import views
from .views import CourList, CourDetail, CourUpdate, CourDelete, CourCreate
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [

   
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('password_reset_done', views.password_reset_done, name='password_reset_done'),
    path('home', CourList.as_view(), name='cour-index'),
    path('cour-detail/<int:pk>/', CourDetail.as_view(), name='cour-detail'),
    path('cour-update/<int:pk>/', CourUpdate.as_view(), name='cour-update'),
    path('cour-delete/<int:pk>/', CourDelete.as_view(), name='cour-delete'),
    path('cour-create', CourCreate.as_view(), name='cour-create'),
   
    
]

