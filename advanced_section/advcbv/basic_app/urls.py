from basic_app import views
from django.urls import include, path

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<str:pk>/', views.SchoolUpdateView.as_view(), name="update"),
    path('delete/<str:pk>/', views.SchoolDeleteView.as_view(), name="delete"),
    path('<str:pk>/', views.SchoolDetailView.as_view(), name="detail"),

]
 