from django.urls import path
from .views import post_detail, post_view

app_name = 'blogapi'

urlpatterns = [
    path('<int:pk>/', post_detail, name='detailcreate'),
    path('', post_view, name='listcreate'),
]