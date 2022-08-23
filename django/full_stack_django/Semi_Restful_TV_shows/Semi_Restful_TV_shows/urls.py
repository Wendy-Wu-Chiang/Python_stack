
from django.urls import path, include
# from tv_show_app import views

urlpatterns = [
    # path('', views.index),
    path('shows/', include('tv_show_app.urls')),
]
