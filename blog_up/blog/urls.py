from django.urls import path
from . import views


urlpatterns = [
    path("search/", views.SearchResultView.as_view(), name='search'),
    path('', views.index, name='index'),
    path('article/<slug:slug>/<int:id>', views.blog_details, name='details'),

    path('django/', views.django_index, name='django_index'),
    path('python/', views.python_index, name='python_index'),
    path('linux/', views.linux_index, name='linux_index'),
    path('windows/', views.windows_index, name='windows_index'),
    path('mikrotik/', views.mikrotik_index, name='mikrotik_index'),
]
