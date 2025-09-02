from django.urls import path
from .views import index, contact, search, create

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),

    # CRUD operations for contacts
    path('contact/<int:contact_id>/', contact, name='contact'),
    path('contact/create/', create, name='create'),
]