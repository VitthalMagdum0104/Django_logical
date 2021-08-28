from django.urls import path
from .views import array_addition, palindrome_check, index

urlpatterns = [
    path('array_addition/', array_addition, name='array_addition'),
    path('array_addition/<int:number>/', array_addition, name='array_addition'),
    path('palindrome_check/', palindrome_check, name='palindrome_check'),
    path('palindrome_check/<str:string>/',
         palindrome_check, name='palindrome_check'),
    path('index/', index, name='index'),
]
