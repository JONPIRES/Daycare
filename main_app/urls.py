from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('kids/', views.kids_index, name ='index'),
     path('kids/<int:kid_id>/', views.kids_detail, name='detail'),
    # the "<>" after the "/" work similar to the req.params in express
    path('kids/create/', views.KidCreate.as_view(), name ='kid_create'),
    path('kids/<int:pk>/update', views.KidUpdate.as_view(), name ='kid_update'),
    path('kids/<int:pk>/delete', views.KidDelete.as_view(), name ='kid_delete'),
    path('kids/<int:kid_id>/add_feeding', views.add_feeding, name ='add_feeding'),

]