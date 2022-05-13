from basic_app import views
from django.urls import include, path

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<str:pk>/', views.SchoolDetailView.as_view(), name="detial"),

]
