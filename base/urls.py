from django.urls import path 
from base.views import home ,search,contact,showall,find,find_like


urlpatterns = [

    path('home',home),
    path('search/',search),
    path('find',find),
    path('find_like',find_like),
    path('contact',contact),
    path('all',showall),
]