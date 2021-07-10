from django.urls import path
from . import views


urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

]
