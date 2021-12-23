from django.urls import path
from . import views

app_name = "vote"
urlpatterns = [
     path('', views.index, name="index"),
     path('datail/<tpk>',views.detail,name='detail'),
     path('vote/<tpk>',views.vote, name='vote'),
     path('cancel/<tpk>',views.cancel,name='cancel'),
     path('create',views.create,name='create')

]