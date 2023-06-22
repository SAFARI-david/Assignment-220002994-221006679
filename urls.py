from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_view, name='create'),
    path('<int:pk>/', views.detail_view, name='detail'),
    path('<int:pk>/update/', views.update_view, name='update'),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
]
from django.urls import path
from .views import field1CreateView, field1DetailView, field1UpdateView, field1DeleteView
urlpatterns = [
    path('create/', field1CreateView.as_view(), name='field1_create'),
    path('detail/<int:pk>/', field1DetailView.as_view(), name='field1_detail'),
    path('update/<int:pk>/', field1UpdateView.as_view(), name='field1_update'),
    path('delete/<int:pk>/', field1DeleteView.as_view(), name='field1_delete'),
]
