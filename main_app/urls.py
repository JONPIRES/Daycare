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
    path('kids/<int:pk>/delete_feeding', views.FeedingDelete.as_view(), name ='feeding_delete'),

    # toys paths
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name ='toys_detail'),
    path('toys/create', views.ToyCreate.as_view(), name ='toys_create'),
    path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name ='toys_update'),
    path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name ='toys_delete'),
    path('toys/<int:kid_id>/assoc/<int:toy_id>/', views.assoc_toy, name ='assoc_toy'),
    path('toys/<int:kid_id>/remove/<int:toy_id>/', views.remove_toy, name ='remove_toy'),
]