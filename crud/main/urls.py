from django.urls import path
from .views import HomeListView, NameCreateView, NameUpdateView, NameDeleteView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('create/', NameCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NameUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NameDeleteView.as_view(), name='delete'),
]
