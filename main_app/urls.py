from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('kids/', views.kids_index, name ='index'),
    # the "<>" after the "/" work similar to the req.params in express
    path('kids/<int:kid_id>', views.kids_detail, name ='detail')
]