# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home/',view=views.home,name='home'),
    path('contact/',view=views.contact,name='contact'),
    path('about/',view=views.about,name='about'),
    path('product/', view=views.product,name='product'),
    path('staff/',view=views.staff,name='staff'),
    path('stafflist/',view=views.stafflist,name='stafflist'),
    path('detail/<int:id>',view=views.detail,name='detail'),

]