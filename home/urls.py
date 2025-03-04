from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name = 'home'),
    path('add/' , views.addBook , name = 'addBook'),
    path('update/<int:id>/' , views.updateBook , name='updateBook'),
    path('delete/<int:id>/' , views.deleteBook , name='deleteBook'),
]