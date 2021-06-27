from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name ='index'),
    path('socio',views.socio, name ='socio'),
    path('about',views.about, name ='about'),
    path('contact',views.contact, name ='contact'),
    path('detail_image',views.detail_image, name ='detail_image'),
]
