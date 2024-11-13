from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('admin/', views.admin_view, name='admin_page'),
    path('delete/<int:url_id>/', views.delete_url, name='delete_url'),  # URL to delete a URL
    path('view/<int:url_id>/', views.redirect_url, name='redirect_url'),  # Redirect shortened URL to original URL
]
